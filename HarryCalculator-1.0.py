print ("Number 1")
num1 = int(input())
print ("Number 2")
num2 = int(input())
print ("Operation (+, -, *, or /)")
op = input()
if op == "+":
    ans = num1 + num2
elif op == "-":
    ans = num1 - num2
elif op == "*":
    ans = num1 * num2
elif op == "/":
    ans = num1 / num2
else:
    print ("Unknown Operator")
    exit()
print (ans)

