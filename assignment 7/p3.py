#Write a program to check whether a given number is there in the Fibonacciseries or not.
num=int(input("Enter number: "))
fib1=0
fib2=1
fib3=1
if((num==0) or (num==1)):
    print(num," is in fibonaci series.")
else:
    fib3=fib1+fib2
    while(fib3<num):
     fib1=fib2
     fib2=fib3
     fib3=fib1+fib2
    if(fib3==num):
       print(num," is in fibonaci series.") 
    else:
       print(num,"is not in fibonaci series")