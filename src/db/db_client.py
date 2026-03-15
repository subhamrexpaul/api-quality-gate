import sqlite3


class DBClient:
    """
    SQLite database client for storing and querying API test results.
    Uses Python's built-in sqlite3 module — no pip install needed.
    """

    def __init__(self, db_name: str = "test_results.db"):
        """
        Connect to a SQLite database file.

        :param db_name: Name of the SQLite database file (default: test_results.db)
        """
        # sqlite3.connect() creates the file if it doesn't exist
        self.connection = sqlite3.connect(db_name)
        # Row factory allows us to access columns by name (like a dict)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
