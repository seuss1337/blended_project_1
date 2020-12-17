import machine_learning as ML
import sql_methods as SQLM

print(SQLM.gets_sample_df(10, 5))
SQLM.save_df_as_sqlite(SQLM.gets_sample_df(10, 5))
print(ML.isWorking())

