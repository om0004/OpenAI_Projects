import sqlalchemy
from sqlalchemy import create_engine,text

def convert_to_database(df,table_name):
    temp_db = create_engine('sqlite:///:memory:',echo=False)
    df.to_sql(name=table_name,con=temp_db)
    with temp_db.connect() as conn:
        result = conn.execute(text("select sum(sales) from Sales"))
    print(result.all())

def create_SQL_prompt(df,table_name):
    prompt = """ This is a sqlite SQL table, with its properties:
    {}({})
""".format(table_name,",".join([str(col) for col in df.columns]))
    
    return prompt
    

