t = (1, 2, 3)
a, b, c = t
print("1st:" + str(a), "2nd:" + str(b), "3rd:" + str(c))

users = [
    {"name": "Andrew", "age": 16},
    {"name": "John", "age": 25},
    {"name": "Alex", "age": 20}
]

sorted_users = sorted(users, key=lambda u: u["age"])
print(sorted_users)