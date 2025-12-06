class Student:
    def __init__(self,name,father_name,age):
        self.name = name
        self._father_name = father_name
        self.age = age

a = Student("Asif","Amjad", 19)
b = Student("Hussnain","Amjad", 9)
print("Student - 1\n")
print("Name :",a.name,"\nFather Name :",a._father_name,"\nAge :",a.age)
print("\nStudent - 2\n")
print("Name :","\nFather Name :",a.name,a._father_name,"\nAge :",a.age)


