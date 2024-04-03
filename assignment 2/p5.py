#Write a program to input a three-digit number and display the sum of the digits.
number=int(input("Enter three digit number"))
a = number // 100
b = number // 10 % 10
c = number % 10
print(a + b + c)