menuList = []
totalPrice = 0

def showBill():
    print("----- My Food -----")
    for number in range(len(menuList)):
        print(menuList[number])

#def showPrice(totalPrice = 0):
#    totalPrice = sum(priceList)
#    print("Total :", totalPrice)

while True:
    menuName = input("Name : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append([menuName, menuPrice])
        totalPrice += menuPrice
showBill()
print("total :", totalPrice)