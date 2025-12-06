detail=[
    {"name":"Muhammad Asif","number":"03276814914"},
    {"name":"Hussnain Ali","number":"03054647593"},
    {"name":"Aqsa","number":"03180418756"},
    {"name":"Naeem","number":"03114424370"}
]
#print(f"Here are the Contacts:  {detail}")
#print(detail)
name = (input("Name: "))
for name in detail:
    if name == detail["name"]:
        print("Found")