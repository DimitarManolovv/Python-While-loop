username = input("name: ")
password = input("password:")

while True:
    login_password = input("password: ")
    if login_password == password:
        print(f"Welcome {username}!")
        break
    else:
        print("Wrong password. Try again!")

