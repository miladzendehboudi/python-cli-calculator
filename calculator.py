print("=== Python Calculator ===")

print("1) Addition")
print("2) Subtraction")
print("3) Multiplication")
print("4) Division")

choice= input("Choose an operation: ")

a= float(input("Enter the first number: "))
b= float(input("Enter the second number: "))

if choice == "1":
    result = a+b
elif choice == "2":
    result = a-b
elif choice == "3":
    result = a*b
elif choice == "4":
    if b == 0:
        result = "Error: Division by zero is not allowed!"
    else:
        result = a/b
else:
    result = "Invalid option!"

print("Result:", result)