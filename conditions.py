#voting eligibility checker program
age=int(input("Enter your age: "))
if age >= 18:
    print(f"Since you are {age}, you are eligible to vote.")
else:
    print(f"Since you are {age}, you are not eligible to vote. You are too young.")
    #a program to check if a number is even or odd
num=int(input("Enter a number: "))
if num%2==0:
    print(f"The number entered({num}) is an even number.")
else:
    print(f"The number entered({num}) is an odd number.")