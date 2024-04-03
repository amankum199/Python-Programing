#Write a program to check whether roots of a given quadratic equation are real & distinct, real & equal or imaginary roots
a=int(input("Enter the value of a "))
b=int(input("Enter the value of b "))
c=int(input("Enter the value of c "))
print("Given quadratic equation is: ",a,"x**2  +  ",b,"x +  ",c)
d=b**2 -4*a*c
print(d)
if d>0:
    print("Real and equal")
elif d<0:
    print("Imajinaray roots")
elif d==0:
    print("Real and distinct")
     