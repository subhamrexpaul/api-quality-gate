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

    def create_table(self):
        """
        Create the 'bookings' table if it doesn't already exist.
        Stores API response data for SQL-based data integrity testing.
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                booking_id INTEGER,
                firstname TEXT,
                lastname TEXT,
                totalprice INTEGER,
                depositpaid INTEGER,
                checkin TEXT,
                checkout TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        # Commit the DDL statement so the table persists
        self.connection.commit()
