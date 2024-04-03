#Write a program to check whether a given character is an alphabet (uppercase), an alphabet (lower case), a digit or a special character.
ch=input("Enter to check: ")
if (ch >= 'A' and ch <= 'Z'):
    print(ch,"is an UpperCase character")
elif(ch >= 'a' and ch <= 'z'):
    print(ch,"is an LowerCase character")
else:
    print(ch,"is not an alphabetic character")
 