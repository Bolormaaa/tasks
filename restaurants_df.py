from numpy import inner
import pandas as pd
import sqlalchemy as db
from sqlalchemy import create_engine

CONN_STR = 'mysql+pymysql://{2}:{3}@{0}:{4}/{1}'.format(
    'localhost',
    'userdb',
    'root',
    'Akino_sama0204',
    3306
)
engine = db.create_engine(CONN_STR)

connection=engine.connect()

df=pd.read_sql("select * from restaurants", connection)
print(df)

connection.close()

matched_df = df[df["dundaj_une"] >= 20000]
print(matched_df)

duurguud_df=df.groupby('duureg')
fill_mean_df = duurguud_df.mean()
print(fill_mean_df)

def mulltiply_2(x):
   return x*2
df["dundaj_une"] = df["dundaj_une"].apply(mulltiply_2)
print(df)


