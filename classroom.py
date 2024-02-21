class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def printFullname(self):
        print(self.firstname + ", " + self.lastname)

class Student (Person):
    def __init__(self, firstname, lastname, subject):
        super (Student, self).__init__(firstname, lastname)
        self.subject = subject
    def subject(self):
        return self.subject
    def printNameSubject(self):
        print(self.firstname + ", " + self.lastname + ", " + self.subject)
    
class Teacher (Person):
    def __init__(self, firstname, lastname, course):
        super (Teacher, self).__init__(firstname, lastname)
        self.course = course
    def course(self):
        return self.course
    def printNameCourse(self):
        print(self.firstname + ", " + self.lastname + ", " + self.course)