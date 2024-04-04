#Write a program to check whether a given number is a Prime number or not
number=int(input("Enter number: "))
for i in range(2,number,1):
    if(number%i==0):
     print("Not prime")
    else:
       print("Prime")
    break
