#Write a program to calculate factorial of a number
a=int(input("Enter number: "))
m=1
for i in range(a,0,-1):
    m=m*i
print("Factorial of a number is ",m)
