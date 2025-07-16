operator = input ("Enter an oerator (+-*/):")
num1 = float(input ("Enter the first number: "))
num2 = float(input ("Enter the second  number: "))

if operator =="+":
    result = num1 + num2
    print(round(result, 3))
elif operator =="-":
    result = num1 - num2
    print(round(result, 3))
elif operator =="*":
    result = num1 * num2
    print(round(result, 3))
elif operator =="/":
    result = num1 / num2
    print(round(result, 3))
else:
    pint(f"{operator } i not a valid opertor")
