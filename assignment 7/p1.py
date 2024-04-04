#Write a program to find the Nth term of the Fibonnaci series
num=int(input("Enter number: "))
fib1=0
fib2=1
fib3=1
#print("Fibonaci series are: ")
for i in range(1,num+1,1):
    fib=fib1
    #print(fib1,end=" ")
    fib3=fib1+fib2
    fib1=fib2
    fib2=fib3
print(num,"th term of fibonaci series are: ",fib)