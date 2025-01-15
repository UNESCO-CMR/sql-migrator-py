## About

This project allows you to migrate one or more local or cloud SQL files to a local or remote MySQL database and track the progress.

## Getting Started
> If you already have a large database file (SQL) and you need to smartly split it into small chuncks, I added a .exe binary [SQLDumpSlitter.rar](SQLDumpSplitter.rar) by Philip Lehmann-Bohm. After the split, you may need to first run ...DataStructure.sql which has the structure of your database. 

To use this application, follow the steps below:

### Prerequisites

- Python v3 Interpreter installed on your computer system. Download it from: [https://python.org/downloads](https://python.org/downloads).
- Ensure that Python is added to your path variables.

### Installation

1. Clone the project to your computer:

```
$ git clone https://github.com/UNESCO-CMR/sql-migrator-py.git
```

2. Open the command line/terminal and navigate to the project directory:

```
$ cd sql-migrator-py
```

3. Install the required Python dependencies (mysql-connector-python) from the requirements file:

```
$ python -m pip install -r requirements.txt
```

### Usage

1. Before running the script, make sure that the `mysql` command is accessible from the terminal. If not, add the directory containing the `mysql` command to your PATH variables.

E.g., On Window and using XAMPP, this will likely be found in the directory `C:\xampp\mysql\bin`. On Mac, this will likely be found in `Applications/XAMPP/bin/mysql`. Add this directory to your PATH variables. Then reopen any closed commandline/terminal before proceeding.

1. Run the script with the following parameters:

- `[SQL_DIR]`: The path to the directory containing the SQL files (required).
- `[DATABASE]`: Your database name (required).
- `[USERNAME]`: Your database user (required).
- `[PASSWORD]`: Your database user's password (optional, default: ""). 
> Do not enter your password. Simple add the -p or --password argument & you'll be prompted to enter it.
- `[HOST]`: Your MySQL Host name (optional, default: localhost or 127.0.0.1).
- `[PORT]`: Your MySQL Port address (optional, default: 3306).
- `[PROGRESS_FILE]`: Text file to store import progress (optional, default: counter.txt).

Example command:

```
$ python main.py --sql-dir [SQL_DIR] --database [DATABASE] --username [USERNAME] --password
```
> After adding the -p or --password flag, you will be prompted to enter your password and it won't be visible. When you are done typing it, hit enter. 

### Extra: Execute files sequentially

To execute files sequentially, ensure that the file names are terminated with an underscore and an incremental number. For example: `backup_file_1.sql`, `backup_file_2.sql`, `backup_file_3.sql`, and so on.

## Contributing

Contributions are welcome! 
1. To-do 1: Handling other database systems besides MySQl.
2. To-do 2: Test this app on a cloud server without needing to host this application on that server.
3. If you have any suggestions, improvements, or bug fixes, please submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

Thank you to all content-producers on the internet.

If you have any questions or need further assistance, please feel free to contact us.