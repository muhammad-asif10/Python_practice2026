class Person():
    name = 'Muhammad Asif'
    father_name = 'Amjad Ali'
    age = 19
a = Person()
print('Name:    ',a.name ,'\nFather_name:    ', a.father_name,'\nAge:    ', a.age) #Before changing the name - Asif
a.name= 'Hussnain Ali'
a.father_name='Amjad Ali'
a.age=10
print('Name:    ',a.name ,'\nFather_name:    ', a.father_name,'\nAge:    ', a.age) #After changing the name - Hussnain
a.name = 'Aqsa'
a.father_name= 'Amjad Ali'
a.age= 21
print('This is detail of "Aqsa Bibi"')
print('Name:    ',a.name ,'\nFather_name:    ', a.father_name,'\nAge:    ', a.age) #--Aqsa



