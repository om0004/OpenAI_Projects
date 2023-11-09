import openai,os

def create_SQL_prompt(df,table_name):
    prompt = """ This is a sqlite SQL table, with its properties:
    {}({})
""".format(table_name,",".join([str(col) for col in df.columns]))
    
    return prompt
def combine_prompts(sql_prompt,user_input):
    query = f" A SQL query to answer: {user_input}"
    return sql_prompt+query

def send_to_openai(prompt):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    response = openai.Completion.create(
        model = 'gpt-3.5-turbo-instruct',
        prompt = prompt,
        max_tokens = 150,
        temperature = 0
    )
    return response['choices'][0]['text']
