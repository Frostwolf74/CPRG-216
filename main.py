num1 = int(input("Enter a number: "))
op = input("Enter operator(+,-,*,/): ") # add sq rt later
num2 = int(input("Enter the next number: "))

if op == "+":
    ans = num1 + num2
elif op == "-":
    ans = num1 - num2
elif op == "*":
    ans = num1 * num2
elif op == "/":
    ans = num1 / num2

print(ans)
