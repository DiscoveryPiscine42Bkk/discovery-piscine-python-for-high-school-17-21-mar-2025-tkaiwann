#!/usr/bin/env python3
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
ans = first_number * second_number
print(f"{first_number} x {second_number} = {ans}")
if ans > 0 : print("The result is positive")
elif ans < 0 : print("The result is negative")
else : print("The result is positive and negative")