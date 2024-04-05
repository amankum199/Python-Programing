#Write a program to find next Prime number of a given number
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_next_prime(number):
    next_number = number + 1
    while True:
        if is_prime(next_number):
            return next_number
        next_number += 1

# Example usage
given_number = int(input("Enter number: "))
next_prime = find_next_prime(given_number)
print(f"The next prime number after {given_number} is {next_prime}.")