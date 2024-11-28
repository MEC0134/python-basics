# This is a python comment and below is a multi-line comment


"""
Python Varibales

Normally we do not explicitly specify data type in python when declaring variables,
we can however apply casting to a variable using built in methods as
demonstrated below
"""

x = int(3)
z = float(3)

# print(x, z)


# Getting the data type of variables
print(type(x))
print(type(z))




"""
Rules for naming variables in Python
    
    - Variable name must start with letter or underscore
    - It cannot start with number
    - Variable names can only contain alpha-numeric values (A-z, 0-9, and _)
    -  Variable names are case-sensitive (age, Age and AGE are three different variables)
    - A variable name cannot be any of the Python keywords.

"""



# There are no differences in single or double quotes in python
exName = "John"
# is the same as
exName = 'John'


# Python variable names are case-sensitive, a and A will be different variables
a = "This var is not A"
A = "and this var is not a"


"""
Multi Words Variable Names

    3 methods to name multi word variables
    
        - Pascal Case: VariableName
        - Camel Case: variableName
        - Snake Case: variable_name
"""


""" Assigning Multiple Values at once example below, we can use them separately of course """

car1, car2, car3 = "Mini Cooper", "Toyota", "Bmw"
print("My favorite car out of all cars is " + car3)

""" We can also assign one value to multiple variables as below """

fruit1 = fruit2 = fruit3 = "Apple"
print(fruit2)

""" Unpacking: is the action of breaking/extracting values up a list/tuple into variables as below  """

animals = ['cat', 'dog', 'horse']
animal1, animal2, animal3 = animals
print(animal1)


# Outputting multiple variables at once using print, we can use comma or + sign

print(animal1, animal2, animal3)

# With number data types + will work as a operator not concatenation

print(7 + 7 + 9)

# When outputting different data types we should use comma instead of + as we will get a TypeError

print(7, "is my favorite number")


# Global Variables: variables that are created outside a function and therefor are accessible globally, example:

global_variable = 'My Global Variable'

def my_function():
    print("Here is " + global_variable)

# Call function
my_function()

# Local variables: are variables that are declared within a function and therefor only accessible within the function

def my_function2():
    local_varibale = 'My Local Variable'
    print(local_varibale, "is only accessible here")

my_function2()

"""
Global Keyword: We can use the global keyword to declare a variable as global one within a function, but we cannot assign it directly.
We can also update the value of a global variable inside a function using the global keyword 

"""
def my_function3():
    global global_keyword_variable
    global_keyword_variable = 'Using Global Keyword'

# First we call the function to access variable
my_function3()

print('We are accessing the global var inside my_function3:', global_keyword_variable)

