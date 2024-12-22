import SimCal as Rakib

while True:
    print("Enter 1 to add, \n2 to subtract, \n3 to multiplication, \n4 for division, \n5 for pawer, \n6 for modulo \n 0 to exit")

    choice = int(input("Your Choice:"))

    if choice == 0:
        break

    if choice == 1:
        a = int(input("Enter a:"))
        b = int(input("Enter b:"))
        print(Rakib.add(a, b))
    if choice == 2:
        a = int(input("Enter a:"))
        b = int(input("Enter b:"))
        print(Rakib.sub(a, b))
    if choice == 3:
        a = int(input("Enter a:"))
        b = int(input("Enter b:"))
        print(Rakib.mul(a, b))

    if choice == 4:
        a = int(input("Enter a:"))
        b = int(input("Enter b:"))
        print(Rakib.div(a, b))

    # # Function for pow (a ^ b)

    if choice == 5:
        a = int(input("Enter a:"))
        b = int(input("Enter b:"))
        print(Rakib.pow(a, b))

    # Function for modulo (a % b)
    if choice == 6:
        a = float(input("Enter a:"))
        b = float(input("Enter b:"))
        print(f"The remainder when {a} % is divided by {b} is = {Rakib.modulo(a, b)}")
