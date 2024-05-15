def calculator():
  num1 = float(input("enter first number:  "))
  num2 = float(input("enter second number:  "))
  operator = input("enter operator(+, -, *, /):")
  if operator == "+":
    print("result", (num1 + num2))
  elif operator == "-":
    print("result", (num1 - num2))
  elif operator == "*":
    print("result", (num1 * num2))
  elif operator == "/":
    if num2 == 0:
      print("error division by zero is        not allowed")
    else:
        print("result", (num1 / num2))
  else:
    print("invalid operator")


calculator()
#we  are here again#
