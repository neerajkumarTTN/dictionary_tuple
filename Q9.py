from collections import defaultdict

oldAge={"name": "Aayush", "age": 24}
#oldAge={"name": "Aayush"}
age = oldAge.setdefault('age',)
if age is not None:
    age=age+50
    print("Age key if present age is : ", age)
else:
    age=50
    print("Age is key not present default age is :",age)