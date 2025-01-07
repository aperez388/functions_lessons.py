from determineEligibility import determineEligibility_toGraduate, listOfMovies
# functions are ways to wrap your code into reusable units
# place () after the function to invoke it 

# define a function with def
# only define a function once
# when i pass in a parameter, i am passing in a placeholder for furture information
# def say_hello(name, age, address):
#     print(f"Hello, {name}!")
#     print(f"How are you, {name}?")
#     print(f"{name}, you are {age} years old.")
#     print(f"{name}, you live at {address}.")

# call the function also known as invoking
# pass in information called an argument
# say_hello("Alice", 22, "123 Main St")
# say_hello("Paul", 34, "456 Main St")
# say_hello("Bob", 56, "789 Main St")
# say_hello("Altair", 45, "101 Main St")

# need name, gpa, sat score, how many credits you have


determineEligibility_toGraduate("Alice", 24, 2.5, 800)
determineEligibility_toGraduate("Bob", 23, 2.4, 799)

# 4 parameters
# parameters are found in def function

listOfMovies("The Matrix", 10, "action")
listOfMovies("The Hangover", 5, "comedy")
listOfMovies("The Ring", 3, "horror")
listOfMovies("Mufasa", 2, "animated")


# the return statement is used to return a value from a function

# return = statement used to end a function
#          and send a result back to the caller

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))