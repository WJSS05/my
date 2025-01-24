class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self,name,age,chinese,math,english):
        super().__init__(name,age)
        self.chinese = chinese
        self.math = math
        self.english = english


