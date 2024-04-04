#Write a program to reverse a given number
number=int(input("Enter number: "))
orginalnumber =number
reverse=0
for _ in str(number):
    digit= number%10
    reverse=reverse*10 + digit
    number=number//10
print("reversed number = ",reverse)    
