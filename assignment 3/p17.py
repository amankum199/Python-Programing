s1=int(input("Enter the sides of triangle: "))
s2=int(input("Enter the sides of triangle: "))
s3=int(input("Enter the sides of triangle: "))
print("Valid Triangle") if (((s1+s2)>s3) and ((s2+s3)>s1) and ((s3+s1)>s2)) else print("Invalid triangle") 

