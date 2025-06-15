# Positional Arguments
    # By default, when you create a function in Python, it will keep the order of arguments in the function definition
    # e.g. In the function below, the first argument that goes in will always be printed before the second one. a = 2, b = 1

def my_function(a, b):
    print(a)
    print(b)


my_function(2, 1)


# Keyword Arguments: Position doesn't matter
# You can use keywords when you provide the arguments when you call a function so that there is less confusion which value is assigned to which input parameter.

my_function(b=1, a=2)