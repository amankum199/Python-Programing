#Write a program to check whether a given number is an Armstrong number or notint num, originalNum, remainder, result = 0;
print("Enter an integer: ")
num=int(input())
n=len(str(num))
originalNum = num
result=0
while (originalNum != 0):
        remainder = originalNum % 10
        
        result =result +  (remainder**n)
        originalNum //= 10

if (result == num):
        print(f"{num} is an Armstrong number.")
else:
        print(f"{num} is not an Armstrong number.")
