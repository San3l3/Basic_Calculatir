def calculate(num1, num2, operation):
  if operation == "+":
      return num1 + num2
  elif operation == "-":
      return num1 - num2
  elif operation == "*":
      return num1 * num2
  elif operation == "/":
        if num2 == 0:
            return "Error! Division by zero."
        return num1 / num2
  else:
      return "invalid operation."


num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
operation = input("Enter an operation(+, -, *, /): ")

result = calculate(num1, num2, operation)
print(f"{num1} {operation} {num2} = {result}")
