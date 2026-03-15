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

    def insert_booking(self, data: dict):
        """
        Insert a single booking record into the bookings table.
        Expects a dict matching the API response shape from Restful-Booker.

        :param data: A dict with keys like booking_id, firstname, lastname, etc.
        """
        self.cursor.execute("""
            INSERT INTO bookings (booking_id, firstname, lastname, totalprice,
                                  depositpaid, checkin, checkout)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            data.get("booking_id"),
            data.get("firstname"),
            data.get("lastname"),
            data.get("totalprice"),
            # SQLite doesn't have a BOOLEAN type, so store as 1/0
            int(data.get("depositpaid", False)),
            data.get("bookingdates", {}).get("checkin"),
            data.get("bookingdates", {}).get("checkout")
        ))
        self.connection.commit()

    def run_query(self, sql: str) -> list:
        """
        Execute any raw SQL query and return results as a list of dicts.
        Useful for running validation queries from queries.sql.

        :param sql: The SQL query string to execute.
        :return: A list of dictionaries, one per row.
        """
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        # Convert sqlite3.Row objects to plain dicts for easier assertion
        return [dict(row) for row in rows]

    def close(self):
        """
        Close the database connection.
        Should be called during test teardown to release the DB file.
        """
        self.connection.close()
