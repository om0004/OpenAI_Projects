import sqlalchemy
from sqlalchemy import create_engine,text

def convert_to_database(df,table_name):
    temp_db = create_engine('sqlite:///:memory:',echo=True)
    data = df.to_sql(name=table_name,con=temp_db)
    with temp_db.connect() as conn:
        result = conn.execute(text("select sum(sales) from Sales"))
    print(result.all())    

