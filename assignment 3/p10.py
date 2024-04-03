#Write a program which takes the cost price and selling price of a product from the user. Now calculate and print profit or loss percentage
a=int(input("Enter cost price: "))
b=int(input("Enter selling price: "))
if(a>b):
    d=a-b
    e=(d*100)/a
    print("loss percentage: ",int(e))
elif(b>a):
    d=b-a
    e=(d*100)/a
    print("profit percentage: ",int(e))
