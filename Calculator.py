#make calculator buddy
a, b = map(float, input("Enter two numbers: ").split())

print("Addition:", add(a, b))
print("Subtraction:", sub(a, b))
print("Multiplication:", mul(a, b))
print("Division:", div(a, b))