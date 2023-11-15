import openai
from test_generate import TestGenerator
class Teacher():

    def __init__(self):
        print("Please run create_test() to create the test")

    def create_test(self):
        topic = input("Give a topic for the quiz: ")
        number_of_questions = int(input("Number of questions for the quiz: "))
        number_of_options = int(input("Number of options per Question: "))

        
        self.test = TestGenerator(topic,number_of_questions,number_of_options)
        test_content = self.test.run()

        student_view, answers = self.create_student_view(test_content)
        student_view.popitem()
        return student_view, answers


        
        #response = self.get_response(prompt)
        #return response

    def create_student_view(self,test):
        question_dict = {1:""}
        answer_dict = {1:""}
        questions = 1
        for line in test.split("\n"):
            if line.startswith("Correct"):
                answer_dict[questions] = line
                questions += 1
                question_dict[questions] = ''
            else:
                question_dict[questions] += line + "\n"

        return question_dict, answer_dict           

         
    

if __name__ == "__main__":
    test = Teacher()
    student_view, answers = test.create_test()
    print(student_view)
    print(answers)









        
