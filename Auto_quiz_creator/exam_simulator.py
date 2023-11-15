class Exam:

    def __init__(self,student_view,answers):
        self.student_view = student_view
        self.answers = answers


    def take_exam(self):
        student_answers = {}
        for question_number,question in self.student_view.items():
            print(question)
            answer = input("Enter your answer:")
            student_answers[question_number] = answer
        return student_answers
    
    def grade(self,student_answers):
        correct_answers = 0
        for question, answer in student_answers.items():
            if answer.upper() == self.answers[question].upper()[16]:
                correct_answers+=1
        grade = 100 * correct_answers / len(student_answers)

        if grade < 60:
            passed = "Not passed!"
        else:
            passed = "Passed!"
        return f"{correct_answers} out of {len(student_answers)} correct! You achieved: {grade} % : {passed}"





            

if __name__ == "__main__":

    obj = Exam({1:"first",2:"second"},"ok")
    answers = obj.take_exam()
    grade = obj.take_exam(answers)
    print(grade)
