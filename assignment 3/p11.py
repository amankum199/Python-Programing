#Write a program to take marks of 5 subjects from the user. Assume marks are given out of 100 and passing marks is 33. Now display whether the candidate passed the examination or failed
a=int(input("Enter marks in subject 1:" ))
b=int(input("Enter marks in subject 2:" ))
c=int(input("Enter marks in subject 3:" ))
d=int(input("Enter marks in subject 4:" ))
e=int(input("Enter marks in subject 5:" ))
f=((a+b+c+d+e)/500)*100
print("Pass") if f>=33 else print("Failed")

