# Write a program to print all Prime numbers between two given numbers
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Print all prime numbers under 100
a=int(input("Enter first: "))
b=int(input("Enter second: "))
for num in range(a, b+1):
    if is_prime(num):
        print(num, end=" ")