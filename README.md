## About

This project allows you to migrate one or more local SQL files to a local or remote MySQL database.

## Getting Started

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
$ cd .../sql-migrator-py
```

3. Install the required Python dependencies (mysql-connector-python) from the requirements file:

```
$ python -m pip install -r requirements.txt
```

### Usage

1. Before running the script, make sure that the `mysql` command is accessible from the terminal. If not, add the directory containing the `mysql` command to your PATH variables.

1. Run the script with the following parameters:

- `[SQL_DIR]`: The path to the directory containing the SQL files.
- `[DATABASE]`: Your database name (required).
- `[USERNAME]`: Your database user (required).
- `[PASSWORD]`: Your database user's password (optional, default: "").
- `[HOST]`: Your MySQL Host name (optional, default: localhost or 127.0.0.1).
- `[PORT]`: Your MySQL Port address (optional, default: 3306).

Example command:

```
$ python main.py --sql-dir [SQL_DIR] --database [DATABASE] --username [USERNAME] --password [PASSWORD]
```

### Extra: Execute files sequentially

To execute files sequentially, ensure that the file names are terminated with an underscore and an incremental number. For example: `backup_file_1.sql`, `backup_file_2.sql`, `backup_file_30.sql`, and so on.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

Thank you to all content-producers on the internet.

If you have any questions or need further assistance, please feel free to contact us.