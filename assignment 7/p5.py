#Write a program to check whether two given numbers are co-prime numbers or not
num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
if num1>num2 :
    greater=num1
else:
    greater=num2    
for i in range(2,greater+1):
    if((num1%i==0) and (num2%i==0)):
     print("Not Co-prime")
    else:
     print("Co-prime")
    break


