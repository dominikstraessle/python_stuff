# Oracle Database Context Manager

A Context Manager for Oracle Database access with python.

## Getting Started

### Prerequisites

#### cx_Oracle

* [cx_Oracle](https://github.com/oracle/python-cx_Oracle) - Follow the installation instructions

#### Running Oracle Database

You need a running Oracle Database. For example 12c.

#### Python 3.x.x installed

You need a 3.x.x version of python installed.

### Installing

* [oracle_database_connection](https://github.com/dominikstraessle/python_stuff/blob/master/oracle_dbtools/dist/oracle_dbtools-1.1.tar.gz) - Download the modul from here

```shell
cd /directory/where/module/dist
pip install oracle_dbtools-1.1.tar.gz
```

## Example

A simple example for the usage of the ConnectionManager.


```python
from oracle_dbtools.oracle_dbcm import ConnectionManager, CMError

try:
    with ConnectionManager(('user', 'password', 'connection_info')) as cursor:
        cursor.execute("""select id, name from schema.employees""")
        results = cursor.fetchall()
        for line in results:
            print(line)
        pass
except CMError as e:
    print(e)
```

Example with bind variables. Should be used to avoid many different sqlid's with own execution plans on the database.
See also:
[Python cx_Oracle bind variables](https://stackoverflow.com/a/33882805/7130107)
```python
from oracle_dbtools.oracle_dbcm import ConnectionManager, CMError

try:
    with ConnectionManager(('user', 'password', 'tns')) as cursor:
        # Select with a bind variable :id
        SQL = """select  EMPLOYEE_ID, FIRST_NAME, LAST_NAME from schema.employees where EMPLOYEE_ID = :id"""

        results = []

        for i in range(10, 1):
            # 10 executions with different variables, but every select has the same sqlid and execution plan
            cursor.execute(SQL, id=i)
            results.append(cursor.fetchall())

        for line in results:
            # print the results
            print(line)
        pass
except CMError as e:
    print(e)
```

## Acknowledgments

* [README.md Template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
