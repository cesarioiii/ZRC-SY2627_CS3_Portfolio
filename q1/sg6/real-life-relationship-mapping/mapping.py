class Student:
    def __init__(self, student_id : str, student_name : str):
        self.student_id = student_id
        self.student_name = student_name

    def enrollInCourse(self, course : str):
        course.add_student(self)

class Course:
    def __init__(self, course_id : str, course_name : str):
        self.course_id = course_id
        self.course_name = course_name
        self.students = []

    def add_student(self, student : Student):
        self.students.append(student)

    def get_students(self):
        return self.students

student1 = Student("0000", "king")
course1 = Course("0000", "physics")

course1.add_student(student1)

for student in course1.get_students():
    print(f"Student ID: {student.student_id}, Name: {student.student_name}")
    

