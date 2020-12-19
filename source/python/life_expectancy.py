# Resources
import sqlite3
import pandas as pd

# Create a SQL connection to SQLite database
con = sqlite3.connect("../../data/LIFE_EXPECTANCY_DB.db")
cur = con.cursor()

# The result of a "cursor.execute" can be iterated over by row
for row in cur.execute('SELECT * FROM LIFE_EXPECTANCY_TABLE LIMIT 10;'):
    print(row)

# Read sqlite query results into a pandas DataFrame
life_df = pd.read_sql_query("SELECT * from LIFE_EXPECTANCY_TABLE", con)

# Be sure to close the SQLite db connection
con.close()

# Verify that result of SQL query is stored in the dataframe
print(life_df.head(5))

# Dataframe types
print(life_df.dtypes)

# Dataframe types
print(life_df.dtypes)