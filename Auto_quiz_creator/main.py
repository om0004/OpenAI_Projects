from teacher import Teacher
from exam_simulator import Exam


def main():
    teacher = Teacher()
    student_view, answers = teacher.create_test()
    exam = Exam(student_view,answers)
    student_answers = exam.take_exam()
    print(student_answers)
    grade = exam.grade(student_answers)
    print(grade)


if __name__ == "__main__":
    main()