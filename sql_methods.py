import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd
import numpy as np

#engine = create_engine("sqlite:///hawaii.sqlite")
#Base = automap_base()
#Base.prepare(engine, reflect=True)

def gets_sample_df(rows, columns):
    #returns a dataframe with random variables for testing purpuses
    clist = [i for i in range(columns)]
    return pd.DataFrame(np.random.randint(0,100,size=(rows, len(clist))), columns=list(clist))

def save_df_as_sqlite(export_df):
    engine = create_engine('sqlite:///save_df.sqlite', echo=True)
    sqlite_connection = engine.connect()

    sqlite_table = "export"
    export_df.to_sql(sqlite_table, sqlite_connection, if_exists='fail')
    sqlite_connection.close()
