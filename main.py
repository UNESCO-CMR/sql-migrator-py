import os
import subprocess
import glob
import argparse
import mysql.connector
import re

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
        print(f"Failed to connect to the database: {err}")
        return False


def extract_pending_number(file_name):
    match = re.search(r"_(\d+)\.sql$", file_name)
    if match:
        return int(match.group(1))
    return 0


def migrate_data(sql_files_dir, database_name, username, password):
    # Get a list of SQL files in the directory
    sql_files = glob.glob(os.path.join(sql_files_dir, "*.sql"))
    sql_files.sort(key=extract_pending_number)

    # Iterate over the files and import them one by one
    for sql_file in sql_files:
        # Execute the MySQL command to import the data
        cmd = f"mysql -u{username} --password={password} -D{database_name} < {sql_file}" # cmd = f"mysql -uroot --password= -D{database_name} < {sql_file}"
        result = subprocess.run(cmd, shell=True)

        if result.returncode != 0:
            print(f"Failed to migrate data from SQL file {sql_file}")

        else:
            print(f"Data migration completed for file: {sql_file}")

def main():

    parser = argparse.ArgumentParser(description="Import SQL files into MySQL database.")
    parser.add_argument("--sql-dir", required=True, help="Path to the directory containing SQL files.")
    parser.add_argument("--database", required=True, help="Name of the MySQL database.")
    parser.add_argument("--username", required=True, help="MySQL username.")
    parser.add_argument("--password", default="", help="MySQL password.")
    parser.add_argument("--host", default='localhost', help="MySQL host.")
    parser.add_argument("--port", default=3306, help="MySQL port.")

    args = parser.parse_args()
    print(args)

    # Test database connection
    if not test_database_connection(args.database, args.username, args.password, args.host, args.port):
        return

    migrate_data(args.sql_dir, args.database, args.username, args.password)

    print("All data migrations completed successfully.")

if __name__ == "__main__":
    main()