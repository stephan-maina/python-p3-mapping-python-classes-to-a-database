from config import CONN, CURSOR

class Song:
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    def save(self):
        sql = """
            INSERT INTO songs(name, album)
            VALUES(?, ?)
        """
        CURSOR.execute(sql, (self.name, self.album))
        CONN.commit()  # Commit the changes
        self.id = CURSOR.lastrowid  # Get the ID of the last inserted row

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()  # Commit the changes

    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song

# Create the "songs" table if it doesn't exist
Song.create_table()

# Create and save some songs
hello = Song.create("21", "Roses and Thugs")
dns2 = Song.create("DNS", "DTO Hard")

# Print the IDs of the created songs
print(hello.id)
print(dns2.id)

# Fetch and print all songs from the database
songs = CURSOR.execute("SELECT * FROM songs")
for song in songs:
    print(song)

# Close the cursor and the connection when done
CURSOR.close()
CONN.close()
