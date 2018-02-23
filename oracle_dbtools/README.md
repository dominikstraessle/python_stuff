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

## Acknowledgments

* [README.md Template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
