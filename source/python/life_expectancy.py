# Resources
import numpy as np
import sqlite3
import pandas as pd

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import extract
from sqlalchemy import select
from sqlalchemy.orm import join
from sqlalchemy.sql import func
from sqlalchemy import or_
from sqlalchemy import inspect

##################################
# Database Setup
##################################

# https://docs.sqlalchemy.org/en/14/core/engines.html#sqlite
# Module 9 Challenge
engine = create_engine(r'sqlite:///../../data/LIFE_EXPECTANCY_DB.db')

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Happiness = Base.classes.HAPPINESS_TABLE
Expectancy = Base.classes.EXPECTANCY_TABLE

# Tables in database
Base.classes.keys()

# Create our session (link) from Python to the DB
session = Session(engine)

inst = inspect(Expectancy)
Expectancy_columns = [c_attr.key for c_attr in inst.mapper.column_attrs]

# Columns of EXPECTANCY_TABLE
print('Columns for Expectancy Table')
print(Expectancy_columns)

inst = inspect(Happiness)
Happiness_columns = [c_attr.key for c_attr in inst.mapper.column_attrs]

# Columns of HAPPINESS_TABLE
print('Columns for Happiness Table')
print(Happiness_columns)

expect_results = []

# Query contents of EXPECTANCY_TABLE to list
expect_results = session.query(
    Expectancy.ID,
    Expectancy.COUNTRY,
    Expectancy.YEAR,
    Expectancy.STATUS,
    Expectancy.EXPECTANCY,
    Expectancy.MORTALITY,
    Expectancy.INFANT_DEATH,
    Expectancy.ALCOHOL,
    Expectancy.EXPENDITURE_PERCENT,
    Expectancy.HEPATITUS_B,
    Expectancy.MEASLES,
    Expectancy.BMI,
    Expectancy.UNDER_FIVE_DEATH,
    Expectancy.POLIIO,
    Expectancy.EXPENDITURE_TOTAL,
    Expectancy.DIPHTHERIA,
    Expectancy.HIV_AIDS,
    Expectancy.GDP,
    Expectancy.POPULATION,
    Expectancy.THIN_1TO19_YR,
    Expectancy.THIN_5TO9_YR,
    Expectancy.INC_COMPOSITION,
    Expectancy.SCHOOLING
    ).all()

#for temp_result in expect_results:
#    print(temp_result)

# Convert Expectancy list to dataframe
expect_df = pd.DataFrame(expect_results, columns=Expectancy_columns)
print('Expectancy Dataframe')
print(expect_df)

happy_results = []

# Query contents of HAPPINESS_TABLE to list
happy_results = session.query(
    Happiness.ID,
    Happiness.COUNTRY,
    Happiness.REGION,
    Happiness.HAPPINESS_SCORE,
    Happiness.HAPPINESS_RANK,
    Happiness.LOW_CONF,
    Happiness.HIGH_CONF,    
    Happiness.STANDARD_ERROR,
    Happiness.ECONOMY,
    Happiness.FAMILY,
    Happiness.HEALTH,
    Happiness.FREEDOM,
    Happiness.TRUST,
    Happiness.GENEROSITY,
    Happiness.DYSTOPIA,
    Happiness.YEAR
    ).all()

#for temp_result in happy_results:
#    print(temp_result)

# Convert Happiness list to dataframe
happy_df = pd.DataFrame(happy_results, columns=Happiness_columns)
happy_df = happy_df.rename(columns={"HAPPINESS_SCORE":"HAPPINESS_RANK","HAPPINESS_RANK":"HAPPINESS_SCORE"})

print('Happiness Dataframe')
print(happy_df)

# INNER JOIN between Expectancy & Happiness data with filter on Expectancy data to only view 2015 year.

happy_expect_join = []

happy_expect_join_columns = Expectancy_columns + Happiness_columns

happy_expect_join = session.query(
    Expectancy.ID.label("E_ID"),
    Expectancy.COUNTRY,
    Expectancy.YEAR,
    Expectancy.STATUS,
    Expectancy.EXPECTANCY,
    Expectancy.MORTALITY,
    Expectancy.INFANT_DEATH,
    Expectancy.ALCOHOL,
    Expectancy.EXPENDITURE_PERCENT,
    Expectancy.HEPATITUS_B,
    Expectancy.MEASLES,
    Expectancy.BMI,
    Expectancy.UNDER_FIVE_DEATH,
    Expectancy.POLIIO,
    Expectancy.EXPENDITURE_TOTAL,
    Expectancy.DIPHTHERIA,
    Expectancy.HIV_AIDS,
    Expectancy.GDP,
    Expectancy.POPULATION,
    Expectancy.THIN_1TO19_YR,
    Expectancy.THIN_5TO9_YR,
    Expectancy.INC_COMPOSITION,
    Expectancy.SCHOOLING,
    Happiness.ID,
    Happiness.COUNTRY,
    Happiness.REGION,
    Happiness.HAPPINESS_SCORE,
    Happiness.HAPPINESS_RANK,
    Happiness.LOW_CONF,
    Happiness.HIGH_CONF,    
    Happiness.STANDARD_ERROR,
    Happiness.ECONOMY,
    Happiness.FAMILY,
    Happiness.HEALTH,
    Happiness.FREEDOM,
    Happiness.TRUST,
    Happiness.GENEROSITY,
    Happiness.DYSTOPIA,
    Happiness.YEAR
).join(Happiness, func.lower(Expectancy.COUNTRY) == func.lower(Happiness.COUNTRY)
).filter(Expectancy.YEAR == '2015'
).filter(Happiness.YEAR == '2015').all()

happy_expect_join_df = pd.DataFrame(happy_expect_join, columns=happy_expect_join_columns)

print(happy_expect_join_df)

# Columns of the joined data between Expectancy & Happiness
print('Joined Dataframe Columns')
for col in happy_expect_join_df.columns: 
    print(col) 

# Check for NULL values in Happy Dataframe
for column in happy_df.columns:
    print(f'Column {column} has {happy_df[column].isnull().sum()} null values')

# Check for NULL values in Expect Dataframe
for column in expect_df.columns:
    print(f'Column {column} has {expect_df[column].isnull().sum()} null values')   
print('HAPPINESS TABLE SUMMARY')
print(happy_df.describe())
print('*******************************************************************************************')
print('*******************************************************************************************')

print('EXPECTANCY TABLE SUMMARY')
print(expect_df.describe())

# Close DB Session
session.close()