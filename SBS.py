def great_bank_system():
 balance = 0.0
 password = input("set your password: ")

 ent_password = input("Enter yout password: ")
 if password != ent_password:
    print("incorrect password. Access denied")
    return
 else:
    print("Login successful")

 while True:
    print("----Welcome To Winnie's Bank----")
    print("1. check balance")
    print("2. deposit")
    print("3. withdraw")
    print("4. exist")

    choice = input("Enter your choice(1 - 4): ").strip()
    if choice == "1":
       print(f"you have a total balance  of: {balance:.2f}")
    elif choice == "2":
        amount = float(input("Enter deposited amount: "))
        if amount > 0:
          balance += amount
          print("deposited succesfully")
        else:
            print("Invalid amount!")

    elif choice == "3":
          amount = float(input(f"input withdrawal amount: yuu"))
          if amount <= balance and amount > 0:
            balance -= amount
            print("Withrawal successful")
            
          else:
             print("Insufficient fund")  
    elif choice == "4":
       print("Thank you for banking with us, have a nice day!")
       break
    else:
       print("Invalid option, try again")
great_bank_system()

 

