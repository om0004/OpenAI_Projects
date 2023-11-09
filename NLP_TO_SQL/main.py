import os
import logging

import pandas as pd
import openai

import db_utils
import openai_utils
# add API key here
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
openai.api_key = os.getenv('OPENAI_API_KEY')

def main():
    # SQL query will run on this data
    logging.info("Loading data...")
    df = pd.read_csv('data/sales_data_sample.csv')
    logging.info(f"Data format: {df.shape}")
    
    logging.info("Converting to database...")
    # function to convert this dataframe into a database 
    database = db_utils.convert_to_database(df,'Sales')

    # Get SQL prompt with the table definition
    sql_prompt = openai_utils.create_SQL_prompt(df,'Sales')
    logging.info(f"Fixed SQL prompt: {sql_prompt}")

    logging.info(" Waiting for user input...")
    # get input from user and combine it to SQL prompt and send final prompt to openAI
    user_input = input("Write the information you want from the data:")
    final_prompt = openai_utils.combine_prompts(sql_prompt,user_input)
    logging.info(f"Final prompt: {final_prompt}")

    logging.info("Sending to OpenAI...")
    response = openai_utils.send_to_openai(final_prompt).strip()
    logging.info(f"Response from openAI is: {response}")

    result = db_utils.execute_query(database,response)
    logging.info(f"Result: {result}")

if __name__ == "__main__":
    main()