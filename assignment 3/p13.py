#Write a program to check whether a given number is divisible by 3 and divisible by 2.
a=int(input("Enter a number: "))
print("Divisible ") if((a%2==0) & (a%3==0)) else print("Not divisible")
