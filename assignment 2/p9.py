#Write a program to input a number from the user and also input a digit. Append a digit in the number and print the resulting number. (Example - number=234 and digit=9 then the resulting number is 2349)
a=int(input("Enter a number"))
b=int(input("Enter digit"))
c=a//10
d=c*10+b
print(d)