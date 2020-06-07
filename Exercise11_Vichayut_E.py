num = int(input("Number : "))
for x in range(1, num+1):
    for y in range(num - x):
        print(" ", end="")
    for y in range(x * 2 - 1):
        print("*", end="")
    print()