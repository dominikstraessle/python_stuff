from setuptools import setup

setup(
    name='oracle_dbtools',
    version='1.1',
    description=('Tools for Oracle Database access.'),
    author='Dominik Strässle',
    license="MIT",
    keywords="oracle database context manager",
    url="https://github.com/dominikstraessle/python_stuff/tree/master/oracle_database",
    py_modules='oracle_dbcm',
    packages=['oracle_dbtools'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Database",
        "License :: OSI Approved :: MIT License",
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
    ],
)
