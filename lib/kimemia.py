from config import CONN, CURSOR

class Song:
    # Define class variables for table and column names
    TABLE_NAME = 'songs'
    COLUMN_ID = 'id'
    COLUMN_NAME = 'name'
    COLUMN_ALBUM = 'album'

    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        # SQL query to create the "songs" table
        sql = f"""
            CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
                {cls.COLUMN_ID} INTEGER PRIMARY KEY,
                {cls.COLUMN_NAME} TEXT,
                {cls.COLUMN_ALBUM} TEXT
            )
        """

        # Ensure proper handling of database connections and transactions
        try:
            CURSOR.execute(sql)
            CONN.commit()
            print(f"Table '{cls.TABLE_NAME}' created successfully.")
        except Exception as e:
            CONN.rollback()
            print(f"Error creating table: {e}")
        finally:
            CONN.close()
