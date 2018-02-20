# Oracle Database Context Manager

A Context Manager for Oracle Database access.

## Getting Started

### Prerequisites

#### cx_Oracle

[cx_Oracle](https://github.com/oracle/python-cx_Oracle) - Follow the installation instructions

### Installing

[oracle_database_connection](https://github.com/dominikstraessle/python_stuff/blob/master/oracle_database/dist/oracle_database_connection-1.0.tar.gz) - Download the modul from here

```
cd /directory/where/module
pip install oracle_database_connection-1.0.tar.gz
```

## Example

Explain how to run the automated tests for this system

###tabulate for beautiful representation
```
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

