first_number = float(input("Enter the first number here:  "))
second_number = float(input("Enter the second number here:  "))
operation_to_do = input("Enter the operation you want to perform: [+,-,*,/]:  ")

if operation_to_do == "+":
    print(first_number + second_number)
elif operation_to_do == "-":
    print(first_number - second_number)
elif operation_to_do == "*":
    print(first_number * second_number)
elif operation_to_do == "/":
    print(first_number / second_number)
else:
    print("Please enter a valid operation")                