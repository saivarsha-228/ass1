def login():
    username="admin"
    password="1234"

    if username=="admin" and password=="1234":
        return "Login  successfull"
    else:
        return "Login failed"
    
print(login())