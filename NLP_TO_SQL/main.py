import os
import logging

import pandas as pd
import openai

import db_utils

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
openai.api_key = os.getenv('OPENAI_API_KEY')

def main():
    # SQL query will run on this data
    logging.info("Loading data...")
    df = pd.read_csv('data/sales_data_sample.csv')
    logging.info(f"Data format: {df.shape}")
    
    logging.info("Converting to database...")
    # function to convert this dataframe into a database 
    db_utils.convert_to_database(df,'Sales')

    # Get SQL prompt with the table definition
    
    logging.info(" Waiting for user input...")
    # get input from user and combine it to SQL prompt and send final prompt to openAI

    logging.info("Sending to OpenAI...")

if __name__ == "__main__":
    main()