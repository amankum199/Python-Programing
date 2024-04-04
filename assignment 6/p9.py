#Write a program to calculate LCM of two numbers
a=int(input("Enter a = "))
b=int(input("Enter b = "))
if a>b:
    greater =a
else:
    greater =b    
while(True):
    if((greater % a == 0) and (greater % b == 0)):
        lcm = greater
        break
    greater+=1
print("LCM is ", lcm)    

