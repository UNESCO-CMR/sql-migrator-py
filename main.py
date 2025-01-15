import os
import subprocess
import glob
import argparse
import mysql.connector
import re
import logging
import datetime
import colorlog
import threading
from getpass import getpass


# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a StreamHandler and set the formatter
handler = logging.StreamHandler()

formatter = colorlog.ColoredFormatter(
    '%(asctime)s - %(log_color)s%(levelname)s%(reset)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white'
    }
)

# Set the formatter on the handler
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)


def test_database_connection(database, username, password, host="localhost", port=3306):
    try:
        conn = mysql.connector.connect(
            host=host,
            port=port,
            database=database,
            user=username,
            password=password
        )
        conn.close()
        return True
    except mysql.connector.Error as err:
        logger.error(f"Failed to connect to the database: {err}")
        return False


def read_progress(progress_file, file_len=0):
    path = os.path.join(os.getcwd(), progress_file)
    if progress_file and os.path.isfile(path):
        with open(path, 'r') as file:
            data = file.readline()
            if len(data) and data.isdigit() and int(data) < int(file_len): # update: ignore progress if it exceeds file count
                return int(data)
    
    return False


def write_progress(progress_file, progress):
    if progress_file and len(str(progress)):
        path = os.path.join(os.getcwd(), progress_file)
        with open(path, "w") as file:
            file.write(str(progress))
        return True
    
    return False



def extract_pending_number(file_name):
    match = re.search(r"_(\d+)\.sql$", file_name)
    if match:
        return int(match.group(1))
    return 0


def migrate_data(sql_files_dir, database_name, username, password, progress_file):
    # Get a list of SQL files in the directory
    sql_files = glob.glob(os.path.join(sql_files_dir, "*.sql"))
    sql_files.sort(key=extract_pending_number)
    files_len = len(sql_files)

    progress = read_progress(progress_file, files_len)
    resume = False

    if progress:
        yn = input(f"Resume after {progress + 1}/{files_len} ({sql_files[progress]})? (Enter: y for 'Yes' or n for 'No'): ")
        if yn.startswith("y") or yn.startswith("Y"):
            resume = True

    # Iterate over the files and import them one by one. If resume is True, skip up to the nth file
    for index, _ in enumerate(sql_files, start=(progress if resume else 0)):
        sql_file = sql_files[index]
        # Execute the MySQL command to import the data
        cmd = f"mysql --max_allowed_packet=100M -u{username} --password={password} -D{database_name} < {sql_file}" # cmd = f"mysql -uroot --password= -D{database_name} < {sql_file}"
        result = subprocess.run(cmd, shell=True)

        if result.returncode != 0:
            logger.warning(f"{index + 1}/{files_len} Error migrating file {os.path.basename(sql_file)}")

        else:
            # Register progress of migration as a thread
            t = threading.Thread(target=write_progress, args=(progress_file, index))
            t.start()
            t.join()

            logger.info(f"{index + 1}/{files_len} Successfully executed: {os.path.basename(sql_file)}")

def main():

    parser = argparse.ArgumentParser(description="Import SQL files into MySQL database.")
    parser.add_argument("-sd", "--sql-dir", required=True, help="Path to the directory containing SQL files.")
    parser.add_argument("-d", "--database", required=True, help="Name of the MySQL database.")
    parser.add_argument("-u", "--username", required=True, help="MySQL username.")
    parser.add_argument('-p', '--password', default="", action='store_true', dest="password", help="MySQL password.")
    parser.add_argument("--host", default='localhost', help="MySQL host.")
    parser.add_argument("--port", default=3306, help="MySQL port.")
    parser.add_argument("-pf", "--progress-file", default="counter.txt", help="Text file to track progress.")

    args = parser.parse_args()

    if args.password:
        password = getpass()
    else:
        password = ""
    

    # Test database connection
    if not test_database_connection(args.database, args.username, password, args.host, args.port):
        return

    migrate_data(args.sql_dir, args.database, args.username, password, args.progress_file)

    # Migration complete
    write_progress(args.progress_file, "")

    logger.info("All data migrations completed successfully.")

if __name__ == "__main__":
    main()
