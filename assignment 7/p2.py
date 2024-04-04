#Write a program to print first N terms of Fibonacci series
num=int(input("Enter number: "))
fib1=0
fib2=1
fib3=1
print("Fibonaci series are: ")
for i in range(1,num+1,1):
    print(fib1, end=" ")
    fib3=fib1+fib2
    fib1=fib2
    fib2=fib3