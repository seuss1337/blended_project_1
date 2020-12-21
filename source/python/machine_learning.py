# def isWorking():
#   return "yes"
# Resources
import sqlite3
import pandas as pd

# Create a SQL connection to SQLite database
con = sqlite3.connect("../../data/LIFE_EXPECTANCY_DB.db")
cur = con.cursor()

# The result of a "cursor.execute" can be iterated over by row
for row in cur.execute("SELECT * FROM LIFE_EXPECTANCY_TABLE LIMIT 10;"):
    print(row)

# Read sqlite query results into a pandas DataFrame
life_df = pd.read_sql_query("SELECT * from LIFE_EXPECTANCY_TABLE", con)

# Be sure to close the SQLite db connection
con.close()
life_df = pd.get_dummies(life_df, columns=["Country"])
# life_df = pd.get_dummies(life_df, columns=["Developing"])
# Verify that result of SQL query is stored in the dataframe
print(life_df.head(5))

# Dataframe types
print(life_df.dtypes)
# from sklearn.preprocessing import StandardScaler


life_df["Adult Mortality"] = pd.to_numeric(life_df["Adult Mortality"], downcast="float")
life_df["Adult Mortality"] = life_df["Adult Mortality"].fillna(0)

y = life_df["Adult Mortality"]
X = life_df.Year.values.reshape(-1, 1)

# import stuff
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# LinearRegression
model = LinearRegression()

# Fit the model
model.fit(X, y)

# y_pred
y_pred = model.predict(X)
print(y_pred.shape)

# Graph the life expectancy
plt.scatter(X, y)
plt.plot(X, y_pred, color="red")
plt.show()
