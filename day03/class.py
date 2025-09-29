class Student:
    def __init__(self,name,age,year,enroll):
        self.name = name
        self.age = age
        self.year = year
        self.enroll = enroll

        print(age,name)
        

govind = Student('govind',18,2025,555555)
print(govind.age)