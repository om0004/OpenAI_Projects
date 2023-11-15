import os,openai


openai.api_key = os.getenv('OPENAI_API_KEY')

class TestGenerator():
    def __init__(self,topic,number_of_questions,number_of_options):

        self.topic = topic
        self.number_of_questions = number_of_questions
        self.number_of_options = number_of_options

        if self.number_of_questions > 6:
            raise ValueError("Please decrease the number of questions!")
        if self.number_of_options >5:
            raise ValueError("More than 5 possible answers is not supported")

    def run(self):
        prompt = self.create_prompt()
        if self.check_prompt(prompt):
            return self.get_response(prompt)
        else:    
            raise ValueError("Prompt failed validation!")

    def create_prompt(self):

        prompt = """ Make a quiz on the topic {} with {} questions and each question with {} options.
        Also mention the answer of each question in the 'Correct Answer:' format
        """.format(self.topic,self.number_of_questions,self.number_of_options)
        return prompt
    
    def check_prompt(self,prompt):
        print(prompt)
        check = input("Are you happy with the prompt? (y/n):")
        if check.upper() == "Y":
            return True
        return False 
    
    def get_response(self,prompt):
        response = openai.Completion.create(
            model = 'gpt-3.5-turbo-instruct',
            prompt = prompt,
            max_tokens= 256,
            temperature = 0.5
        )
        return response['choices'][0]['text']
        





if __name__ == "__main__":
    obj = TestGenerator("Playstation history",2,3)
    print(obj.run())        