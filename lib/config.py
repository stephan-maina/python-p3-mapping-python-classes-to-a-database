import sqlite3

# Connect to the database
CONN = sqlite3.connect('db/music.db')
CURSOR = CONN.cursor()

# Update data using an SQL query
update_query = """
UPDATE your_table_name
SET column_name = new_value
WHERE some_condition;
"""

# Execute the update query
CURSOR.execute(update_query)

# Commit the changes to the database
CONN.commit()

# Close the cursor and the connection
CURSOR.close()
CONN.close()
