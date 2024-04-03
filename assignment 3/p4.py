#. Write a program to check whether a given number is an even number or an odd number without using % operator.
a=int(input("Enter a number: "))
print("Odd") if (a & 1) else print("Even") 