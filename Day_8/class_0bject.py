# class Student:
#    name="ashim kumar"

# S1=Student()

# print(S1.name)



class Student:
    def __init__(self,fullName):
        self.name=fullName
        print ("adding the new student in database")

s1=Student("anik")   
print(s1.name)    