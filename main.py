class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:

    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


s1 = Student("Sandeep", 31, 70)
s2 = Student("Divya", 26, 80)
s3 = Student("SANDY", 31, 90)

c1 = Course("Python", 2)
a = c1.add_students(s1)
print(a)

b = c1.add_students(s2)
print(b)

c = c1.add_students(s3)
print(c)

print(c1.students[0].name)

print(c1.get_average_grade())