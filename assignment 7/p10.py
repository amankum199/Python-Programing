#Write a program to print all Armstrong numbers under 1000print("Enter an integer: ")
num=999
n=len(str(num))
print("Armstrong number are: ")
for i in range(1,num+1):
        new=i
        result=0
        for j in range(1,i+1):
         remainder = new % 10
        
         result =result +  (remainder**n)
         new //= 10

        if (result == i):
         print(i)
