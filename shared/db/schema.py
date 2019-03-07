"""
    The module for creating database.
    This module is executed at the beginning of run.sh script.

    By default sqlite database is created in shared/db/ directory.
"""
import sqlite3

# TODO Define CREATE TABLE statement
SQL_CREATE_TABLE = \
    """
        Write "CREATE TABLE" statement here!
    """


def create_db():
    """Function for initializing sqlite database."""
    # TODO DB name must be defined
    conn = sqlite3.connect('Define DB name here!')

    cursor = conn.cursor()
    cursor.execute(SQL_CREATE_TABLE)
    conn.commit()


if __name__ == '__main__':
    create_db()
