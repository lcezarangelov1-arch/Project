pin_code = int(input("Enter your pin code: "))
balance = 1000

while True:
    if pin_code != 1234:
        pin_code = int(input("Enter your pin code: "))
    if pin_code == 1234:
        print("Welcome!")


        menu = int(input("Enter your menu number: \n1 - Balance\n2 - Withdrawing money\n3 - Depositing money\n4 - General Menu\n5 - Exit\n"))
        if menu == 1:
            print(f"{balance}$")
            break
        elif menu == 2:
            print("How much money you want to withdraw?\nEnter your amount:")
            amount = int(input())
            if amount > balance:
                print("Not enough money!")
            elif amount < balance:
                print(f"Successfully withdrawing!Your balance = {balance - amount}$! Goodbye!")

            break
        elif menu == 3:
            print("How much money you want to deposit?\nEnter your amount:")
            amount = int(input())
            balance += amount
            print(f"Your balance now is : {balance}$")
            break
        elif menu == 4:
            print("You're back in general menu!")
            menu = int(input("Enter your menu number: \n1 - Balance\n2 - Withdrawing money\n3 - Depositing money\n4 - General Menu\n5 - Exit\n"))
            if menu == 1:
                print(f"{balance}$\nIf you want to back in general menu : press 1")
                break
            elif menu == 2:
                print("How much money you want to withdraw?\nEnter your amount:")
                amount = int(input())
                if amount > balance:
                    print("Not enough money!")
                elif amount < balance:
                    print(f"Successfully withdrawing!Your balance = {balance - amount}$! Goodbye!")

                break
            elif menu == 3:
                print("How much money you want to deposit?\nEnter your amount:")
                amount = int(input())
                balance += amount
                print(f"Your balance now is : {balance}$")
                break

        else:
            print("Have a nice day!")
            break










