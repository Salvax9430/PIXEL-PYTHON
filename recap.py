print("welcome to python programming")
# variables.
name = "Bramuel"
x= 45
school= "Emobillis"
print(name)
print(x)
print(school)
print(f"I'm {name} and i like number {x} and {school} is my current school")
# operators 
# arithmatic operators ( +, -, *, /, %, **, //)
x=7
t=56
print(type(x))
sum=x+t
product=x*t
difference=x-t
print(f"The sum of {x} and {t} is {sum}")
print(f"The difference of {x} and {t} is {difference}")
print(f"The product of {x} and {t} is {product}")
print(f"The quotient of {x} and {t} is {x/t}")
# comparison operators (==, !=, >, <, >=, <=)
d=5
e=10
print(e!=d)
print(d==e)
print(e>=d)
# logical operators (and, or, not)
print(d and e)
print(d or e)
print(not d)

 #datat types
# string, integer, float, boolean, list, tuple, set, dictionary
name="Bramuel"
age=576
GPA=3.56
is_student=False
print(type(name))
print(type(age))
print(type(GPA))
print(type(is_student))
# input and output
name=input("Enter your name: ")
age=input("Enter your age: ")
Age=int(input("Enter your age: "))
print(type(name))
print(type(age))
print(type(Age))

# a program to calculate the age
cerrentYear= int(input("Enter the current year: "))
BirthYear= int(input("Enter your birth year: "))
age = cerrentYear-BirthYear
print ( f" Hi {name} you are {age} years old ")
# conditional statements
AGE=int(input("Enter your age: "))
is_registered_as_voter=input("Are you registered as a voter? (yes/no): ")
if AGE>=18 and is_registered_as_voter.lower()=="yes":
    print(f"Since you are {AGE} years old and registered as a voter, you are eligible to vote.")
else:
    print(f"Since you are {AGE} years old and not registered as a voter, you are not eligible to vote.")

 # cheking the larger from 3 numbers
    num1 = int(input("Enter the first number: "))   
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    num4 = int(input("Enter the fourth number: "))
    if num1 >= num2 and num1 >= num3 and num1 >= num4:
        print(f"The largest number is {num1}.")
    elif num2 >= num1 and num2 >= num3 and num2 >= num4:
        print(f"The largest number is {num2}.")
    elif num3 >= num1 and num3 >= num2 and num3 >= num4:
        print(f"The largest number is {num3}.")
    else:
        print(f"The largest number is {num4}.")
