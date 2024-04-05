#Write a program to print all Prime numbers under 100def is_prime(n):
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Print all prime numbers under 100
for num in range(2, 100):
    if is_prime(num):
        print(num, end=" ")