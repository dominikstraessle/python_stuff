from cx_Oracle import Connection, Cursor, Error, ProgrammingError, InterfaceError


class CMError(Exception):
    pass


class CMInterfaceError(CMError):
    pass


class CMProgrammingError(CMError):
    pass


class ConnectionManager:
    """Context Management Protocol for Database access.
    Implementation for accessing Oracle Databases."""

    def __init__(self, config: tuple) -> None:
        """config should contain the following Infromation:
            (username, password, connection_info)"""
        self.config = config
        pass

    def __enter__(self) -> Cursor:
        """Returns a cursor for the interaction with the db"""
        try:
            self.connection = Connection(*self.config)
            self.cursor = self.connection.cursor()
            return self.cursor
        except ProgrammingError as e:
            raise CMProgrammingError(e)
        except InterfaceError as e:
            raise CMInterfaceError(e)
        except Error as e:
            raise CMError(e)
        except Exception as e:
            raise CMError(e)
            pass

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Commits the buffered interactions and closes the cursor and the connection"""
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        if exc_type:
            raise exc_type(exc_val)
        pass
