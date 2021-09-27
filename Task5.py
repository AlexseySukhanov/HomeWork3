x=int(input("Enter a first number "))
y=int(input("Enter a second number "))
z=int(input("Enter a third number "))

if x>y and x>z :
    max=x
elif y>z:
    max=y
else:
    max=z

print(f"Largest number is {max}")