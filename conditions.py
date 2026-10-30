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
    #create a ptyhton script that checks the largest number in three inputs
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    num3=int(input("Enter the third number: "))
    if num1 >= num2 and num1 >= num3:
        print(f"The largest number is {num1}.")
    elif num2 >= num1 and num2 >= num3:
        print(f"The largest number is {num2}.")
    else:
        print(f"The largest number is {num3}.")