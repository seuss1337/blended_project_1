# Life_Expectancy_Analysis
[UT Data Analysis and Visualization Boot Camp Group Project](https://techbootcamps.utexas.edu/data/)

Group repository:  https://github.com/seuss1337/blended_project_1

Contributors:
* https://github.com/seuss1337
* https://github.com/ducluu27 https://www.linkedin.com/in/jpes/
* https://github.com/jt-schmidt https://www.linkedin.com/in/jns04/

## Communication Protocols
We communicated mainly through slack and occasionally text.

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
For this project we selected 2 data sets to merge. The first data we selected was life expectancy and the second one was world happiness. We will be merging these 2 datasets on the country and build a linear regression model.

* Source data:  https://www.kaggle.com/kumarajarshi/life-expectancy-who
* Single table:  LIFE EXPECTANCY (2938 rows x 22 columns, 325.63 KB)
* Time period is 2000 to 2015
* 193 different countries
* Variety of socioeconomic factors; e.g. immunization data, schooling, GDP

* Source data: https://www.kaggle.com/unsdsn/world-happiness
* Single table:  Happiness rank by scores and country in 2015 (158 rows x 12 columns, about 16.17 KB)
* Table dated in 2015
* 158 countries
* Variety of factors such as economy GDP, family, health expectancy, freedom, etc.
* Happiness was measured on a scale of 1-10

![LIFE_EXPECTANCY_TABLE.png](https://github.com/seuss1337/blended_project_1/blob/feature/jt-schmidt/images/LIFE_EXPECTANCY_TABLE.png)


The question decided as a group was "What are the effect of urban population on happiness?"


Inspiration from kaggle source data:
1. Do various predicting factors, which have been chosen initially, significantly impact the Life expectancy? What are the predicting variables that actually affect the life expectancy?
2. Should a country, having a lower life expectancy value(<65), increase its healthcare expenditure in order to improve its average lifespan?
3. How do Infant and Adult mortality rates affect life expectancy?
4. Do eating habits, lifestyle, exercise, smoking, drinking alcohol etc. have positive or negative correlations with Life Expectancy?
5. What is the impact of schooling on the lifespan of humans?
6. Does drinking alchohol have a positive or negative relationship with Life Expectancy?
7. Do densely populated countries tend to have lower life expectancy?
8. What is the impact of Immunization coverage on life Expectancy?

## Dataset Communication Protocols

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
## Machine Learning Model
Week 1: For the provisonal Machine Learning Model we created a simple linear regression model of the United States' life expectancy from 2000-2015. For the data input we used the year and the output was the life expectancy.

![Image](https://github.com/seuss1337/blended_project_1/blob/main/images/Linear%20Regression%20Model.png)


Week 2: For the preliminary data preprocessing, the data for the world happiness and life expectancy only had one overlapping year. So the data was merged on country and removed all data that was not dated in 2015. The next step was to fill in the blanks with 0's. After filling in the data with 0's we decieded to use a logistic regression to predict the developing or developed country with the newly merged data and came up with and 85% accuracy. When creating the logistic regression, we set the y as the status of the developed/developing country and the x as all the other columns. The test data and training data was split into a normal 75% and 25%. Logisitic regression was used because the data allowed us to label the developed/developing countries into 1's and 0's. 

![Image](https://github.com/seuss1337/blended_project_1/blob/feature/duc/images/Logistic_Regression_Prediction.png)
=======
## Presentation

[Presentation Link](https://docs.google.com/presentation/d/1kdANWIdQBFkkx2d57EuJEQaUvLx16OFQzVCG5NjEvvA/edit?usp=sharing)

## Dashboard
[Dashboard Link](https://public.tableau.com/profile/jp4411#!/vizhome/ProjectDashboard_16109429557530/Dashboard3?publish=yes)


