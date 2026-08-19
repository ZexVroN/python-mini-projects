print("=== CALCULATOR V2 ===")
x = int(input("Input x value = "))
y = int(input("Input y value = "))


def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


total_addition = addition(x, y)
print(f"{x} + {y} = {total_addition}")

total_subtraction = subtraction(x, y)
print(f"{x} - {y} = {total_subtraction}")

total_multiplication = multiplication(x, y)
print(f"{x} * {y} = {total_multiplication}")

if y != 0:
    total_division = division(x, y)
    print(f"{x} / {y} = {total_division}")

else:
    print("Sorry, cant divide by zero!")
