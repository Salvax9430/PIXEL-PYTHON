# function to greet
def greet(name):
    print(f"Hello {name}, welcome to the program!")

greet("Bramuel")

def student_info(name, age, course):
    print(f"Student name: {name}")
    print(f"Student age: {age}")
    print(f"Student course: {course}")
    print(f"My name: {name}, and am: {age},i also study: {course}")


student_info("Bramuel", 20, "computer science")
def add_numbers(num1, num2):
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}")
add_numbers(2026, 6044)
def subtract(a,b):
    result=b-a
    print(f"The difference between {b} and {a} is: {result}")
subtract(20, 10)
# functions with inputs to cala cultae discount
def calculate_discount(price, discount_percentage):
    discount = price * (discount_percentage / 100)
    final_price = price - discount
    print(
        f"The initial price was {price}, discount was {discount}, "
        f"and final price is {final_price}"
    )
    return final_price


calculate_discount(7890, 40)


#recap of function i learnt above
def welcome_user():
    print("Welcome to today class")
welcome_user()
def my_name():
    name=input("Enter your name: ")
    age=int(input("Enter your age: "))
    course=input("Enter your course: ")
     
    print(f"My name is {name}, I am {age} years old, and I study {course}.")
    return name, age, course  
my_name()
def age():
    age=int(input("Enter your age: "))
    return age
def class_set(stream):
    print(f"Welcome to the {stream} stream!")
    return stream
result=class_set("Yellow")
print(f"Class set to: {result}")