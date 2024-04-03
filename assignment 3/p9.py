#Write a program to find the greatest among three given numbers. Print number once if the greatest number appears two or three times.
a=int(input("Enter first number" ))
b=int(input("Enter second number" ))
c=int(input("Enter third number" ))
if ((a>b) & (a>c)):
    print(a) 
elif ((b>a) & (b>c)):
    print(b)
elif ((c>a) & (c>b)):
    print(c)