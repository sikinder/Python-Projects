#!/usr/bin/python39
#import math as m

num = int(input("Enter a three digit number: "))

if num<100 or num>999:
    print("Invalid input, not a three digit number!")
    exit()

d1=int(num/100)
d2=int(num%100/10)
d3=int(num%10)

num_reversed=d3*100 + d2*10 + d1
print(num_reversed)

if num == num_reversed:
    print(num," is a palindrome number")
else:
    print(num," is not a palindrome number")
    exit()
    
