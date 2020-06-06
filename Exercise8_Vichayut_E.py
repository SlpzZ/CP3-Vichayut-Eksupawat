userName = input("Username : ")
passWord = input("Password : ")
if userName == "admin" and passWord == "1234":
    print("----- Welcome to M Shop -----")
    print("1.Apple x1 30THB")
    print("2.Banana x1 20THB")
    print("3.Pen x1 10THB")
    goods = int(input("Product : "))
    if goods == 1:
        quan = int(input("Quantity : "))
        total = 30 * quan
    elif goods == 2:
        quan = int(input("Quantity : "))
        total = 20 * quan
    elif goods == 3:
        quan = int(input("Quantity : "))
        total = 10 * quan
    else:
        print("Error!!!")
    print("Total :", total, "THB")
    print("Thank you.")
else:
    print("Username or Password is wrong.!!!")