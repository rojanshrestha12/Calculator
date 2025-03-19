#make calculator buddy

#print("Addition:", add(a, b))
#print("Subtraction:", sub(a, b))
#print("Multiplication:", mul(a, b))
def div(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
a, b = map(float, input("Enter two numbers: ").split())
print("Division:", div(a, b))