def addition():
  a=5
  b=10
  c=a+b
  print (c)
addition()
def division():
  a=5
  b=10
  c=a/b
  print (c)
division()
def greaterThan(a,b):
  if a>b:
    print (a, "is greater than", b)
  else:
    print (b, "is greater than", a)  
greaterThan(10,5)
def 
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