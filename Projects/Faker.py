from faker import Faker
fake =Faker()

print("First Name:    ",fake.first_name())                                      #name
print("Last Name:",fake.last_name())
print("City:",fake.city())
print("Address: ",fake.address())                                   #address
print("Country: ",fake.country())
print("Postal Code:",fake.postalcode())                             #postalcode
print("Phone:   ",fake.phone_number())                              #phonenumber
print("Email:   ",fake.email())                                     #email
print("Job:     ",fake.job())                                       #job
print("Company: ",fake.company())                                   #company
print("Gender:  ",fake.random_element(elements=("Male","Female")))  #Gender
print("Company: ",fake.company())                                   #Company
print("URL:     ",fake.url())
print("Currency",fake.currency_name())  

