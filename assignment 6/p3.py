#Write a program to calculate sum of first N odd natural numbers
a=int(input("Enter number: "))
sum=0
for i in range(1,a+1,1):
    sum=sum+(2*i-1)
print(sum)
