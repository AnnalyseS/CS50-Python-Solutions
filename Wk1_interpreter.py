#prompt user for input
expression = input("Expression: ")
# assign variables to expression
x, y, z = expression.split()
#convert the input into a float
x1 = int(x)
z1 = int(z)
# make the math happen
if y == "*":
    print(float(x1 * z1))
elif y == "/":
    print(float(x1 / z1))
elif y == "+":
    print(float(x1 + z1))
elif y == "-":
    print(float(x1 - z1))