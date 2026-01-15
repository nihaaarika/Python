#WAP to find the greatest of 3 number entered by the user.

a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
c = int(input("enter the third number:"))

if (a>=b and a>=c):
    print("First number is the largest", a)

elif (b>=c):
    print("Second number is the largest", b)

else:
    print("Third number is the largest", c)