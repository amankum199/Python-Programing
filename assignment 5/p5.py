#Write a program to print the first N odd natural numbers in reverse order
a=int(input("Enter number: "))
for i in range(a,0,-1):
    print(2*i-1)