#Write a program to check whether a given number is a three-digit number or not.
a=int(input("Enter a number" ))
print("Three digit number") if len(str(a))==3 else print("Not 3 digit number")