#Write a program to print size of an int, a float, a char and a double type variable
import sys
a=sys.getsizeof(0)
b=sys.getsizeof(0.0)
c=sys.getsizeof("f")
d=sys.getsizeof(0.0)
print(f"Size of int: {a} bytes")
print(f"Size of float: {b} bytes")
print(f"Size of char (string): {c} bytes")
print(f"Size of double (float): {d} bytes")