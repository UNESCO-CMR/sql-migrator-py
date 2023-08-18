## You have many SQL files and wish to import them all at once, here's the solution

### 1. Setup

- Download and Install Python v3 Interpreter on your computer system. 
```Goto: https://python.org/downloads```

| Don't forget to add python to your path variables. This is true to Mac, Linux & Windows.

- Clone the project to your computer:
```$ git clone https://github.com/UNESCO-CMR/sql-migrator-py.git```

- Open the commandline/terminal in the project directory
```$ cd .../sql-migrator-py```

- Install the python dependences (mysql-connector-python) from the requirements file.
```$ python -m pip install -r reqirements.txt```

- ALL DONE ✅

### 2. Run the Script:

##### Parameters
- [SQL_DIR]: The PATH to the directory containing the SQL files. 
- [DATABASE]: Your database name. Required.
- [USERNAME]: Your database user. Required. 
- [PASSWORD]: Your database user's password. Optiona, Default: ""
- [HOST]: Your MySQL Host name. Optional, Default: localhost or 127.0.0.1
- [PORT]: Your MySQL Port address. Optional, Default: 3306

```$ python main.py --sql-dir [SQL_DIR] --database [DATABASE] --username [USERNAME] --password [PASSWORD]```

##### Extra: Execute files sequentially

To execute file sequentially, ensure to terminate the file name with an underscore, then an incremental number.
E.g., backup_file_1.sql, backup_file_2.sql, ..., backup_file_30, .... 