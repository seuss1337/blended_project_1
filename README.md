# Life_Expectancy_Analysis
[UT Data Analysis and Visualization Boot Camp Group Project](https://techbootcamps.utexas.edu/data/)

Group repository:  https://github.com/seuss1337/blended_project_1

Contributors:
* https://github.com/seuss1337
* https://github.com/ducluu27
* https://github.com/jt-schmidt

## Selected Topic: Life Expectancy Data Analysis

## Reason
During group formation & initial discussion, topic brainstorming ranged between:
* Topics of interest; e.g. Spotify podcast, Texas industry growth
* Example datasets; e.g. initial database creation for twitter feeds of top tech companies
* Uniqueness of application: e.g. UCI dataset exploring relation between mobile device accelerometer and alcohol consumption

Ultimately, group determined focus of the assignment should be:
* Cohesive & effective group communication / coordination
* Emphasis on dataset selection where learned principles from the course could be definitvely applied.  Includes:
  * Dataset where machine learning model can be applied
  * Large enough row x column count for sufficient complexity where machine learning is more meaningful
  * Small enough row x column count to easily add dataset to Github repository for demonstration of learned principles

Overall, result of this group project sets foundation for continued growth in learned concepts over past 24 weeks.

## Source Data Overview

* Source data:  https://www.kaggle.com/kumarajarshi/life-expectancy-who
* Single table:  LIFE EXPECTANCY (2938 rows x 22 columns, 325.63 KB)
* Time period is 2000 to 2015
* 193 different countries
* Variety of socioeconomic factors; e.g. immunization data, schooling, GDP

![LIFE_EXPECTANCY_TABLE.png](https://github.com/seuss1337/blended_project_1/blob/feature/jt-schmidt/images/LIFE_EXPECTANCY_TABLE.png)

## Proposed Questions

Inspiration from kaggle source data:
1. Does various predicting factors which has been chosen initially really affect the Life expectancy? What are the predicting variables actually affecting the life expectancy?
2. Should a country having a lower life expectancy value(<65) increase its healthcare expenditure in order to improve its average lifespan?
3. How does Infant and Adult mortality rates affect life expectancy?
4. Does Life Expectancy has positive or negative correlation with eating habits, lifestyle, exercise, smoking, drinking alcohol etc.
5. What is the impact of schooling on the lifespan of humans?
6. Does Life Expectancy have positive or negative relationship with drinking alcohol?
7. Do densely populated countries tend to have lower life expectancy?
8. What is the impact of Immunization coverage on life Expectancy?

Final group decision:  TBD

# Dataset Communication Protocols

[Raw .csv](https://github.com/seuss1337/blended_project_1/blob/feature/jt-schmidt/data/Life%20Expectancy%20Data.csv) loaded into [database](https://github.com/seuss1337/blended_project_1/blob/feature/jt-schmidt/data/LIFE_EXPECTANCY_DB.db) using [SQLite3](https://www.sqlite.org/index.html).  
[Python](https://www.python.org/) with [SQLite3 library](https://docs.python.org/3/library/sqlite3.html) and loaded to [Pandas dataframe](https://pandas.pydata.org/).

``` Python
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
```
