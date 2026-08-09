x = int(input("Input : First number = "))
y = int(input("Input : Second number = "))
operator = str(input("Input : Operator = "))

if operator == "+":
    print(x, "+", y, "=", x + y)

elif operator == "-":
    print(x, "-", y, "=", x - y)

elif operator == "*":
    print(x, "*", y, "=", x * y)

elif operator == "/":
    if y != 0:
        print(x, "/", y, "=", x / y)
    else:
        print(x, "tidak bisa dibagi dengan", y)

else:
    print("Hanya operator ([+], [-], [*], [/]) yang dapat digunakan!")
