#Write a program to take a three-digit number from the user and rotate its digits by one position towards the right
num=int(input("Enter the number"))
a=num//100
b=num//10%10
c=num%10
d=c*100+b*10+a
print(d)
