from calc_tools import calculate

first_text = input("First number: ")
operator = input("Operator (+, -, *, /): ")
second_text = input("Second number: ")

first = float(first_text)
second = float(second_text)

result = calculate(first, operator, second)

if result is None:
    print("Error: invalid operator or division by zero.")
else:
    print(f"{first} {operator} {second} = {result}")