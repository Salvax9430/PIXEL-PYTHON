class Student:
    name="Bramuel"
    age=20
    course="computer science"
#object of the class
# student1=Student()
# print(f"Student name: {student1.name}")
# print(f"Student age: {student1.age}")
# print(f"Student course: {student1.course}")
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
student1=Student("Bramuel",20,"Computer science")
print(student1.name)
print(student1.age)
print(student1.course)
student2=Student("John",22,"Mathematics")
print(student2.name)
student3=Student("Sifuna",20,"Software engineering")

#inheritance
class Animal:
    def speak(self):
        print("Animal speaking")
#child class
class Dog(Animal):
    def speak(self):
        print("Dog barking")