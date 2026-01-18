username = input("Enter your username: ")
password = int(input("Enter your password: "))

while True:
    if username == "Username" and password == 1234:
        print("Successfully logged in")
    else:
        print("Wrong username or password")
        break


    menu = int(input("Select menu option: \nChoose 1 : Show profile\nChoose 2 : Change password\nChoose 3 : Logout\n"))
    if menu == 1:
        print(f"{username} is logged in")
        break
    elif menu == 2:
        print("SET NEW PASSWORD")
        old_password = int(input("Enter your old password: "))
        if old_password == 1234:
            print("Confirm!")
        new_password = int(input("Enter your new password: "))
        password = new_password
        print(f"Password changed!\nYour new password is: {password}\nYour old password is: {old_password}")
    elif menu == 3:
        print("Log out!Have a good day!")

        break


