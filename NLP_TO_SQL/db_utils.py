from sqlalchemy import create_engine,text

def convert_to_database(df,table_name):
    temp_db = create_engine('sqlite:///:memory:',echo=False)
    df.to_sql(name=table_name,con=temp_db,index = False)
    return temp_db

def execute_query(database,SQL_query):
    with database.connect() as conn:
        result = conn.execute(text(SQL_query))
        return result.fetchall()  



