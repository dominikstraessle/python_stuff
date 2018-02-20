# Oracle Database Context Manager

A Context Manager for Oracle Database access.

## Getting Started

### Prerequisites

#### cx_Oracle

* [cx_Oracle](https://github.com/oracle/python-cx_Oracle) - Follow the installation instructions

#### Running Oracle Database

You need a running Oracle Database. For example 12c.

### Installing

* [oracle_database_connection](https://github.com/dominikstraessle/python_stuff/blob/master/oracle_database/dist/oracle_database_connection-1.0.tar.gz) - Download the modul from here

```shell
cd /directory/where/module
pip install oracle_database_connection-1.0.tar.gz
```

## Example

A simple example for the usage of the ConnectionManager.

### tabulate for beautiful representation
```shell
pip install tabulate
```

```python
import connection
from tabulate import tabulate

with connection.ConnectionManager(('user', 'password', 'connection_info')) as cursor:
    cursor.execute("""select id, name from schema.employees""")
    results = cursor.fetchall()
    print(
        tabulate(results, headers=('ID', 'Name'), tablefmt='orgtbl'))
    pass

```

## Acknowledgments

* [README.md Template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
