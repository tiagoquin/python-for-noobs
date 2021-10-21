"""
Chapter 1

Dear reader, let me take you on a Python adventure!

You're currently reading a documentation 'comment'
everything in-between quotation marks 
is not what you'd call 'code' (interpreted)

Follow along by reading the comments
and learn about programming
"""

# text after a hash is a one line comment

# 1/ assignement: you affect a variable with a value
# e.g:      variable = value
arbitrary_name = 1

# 2/ arithmetic: you can use operators between values
# to compute something more complex.
sum = 1 + 2 + 3 + 4

"""
3/  types: a value you can assign to a variable
    has an underlying type. 
    A type describes the representation of it's content
    and the operations you can do on it.

    Example: you can add two numbers together, as well
    as substract, multiply or divide. + - * /
"""

# the variable named one is an integer
one = 1

# phi is a variable of type float
# (floating point number)
phi = 1.618033988749895

# lie is a boolean. It can be either true or false
lie = False
veracity = True

# quote is a string variable.
# it can hold text
quote = "be or not to be"

# None is a special type
# it represents an empty variable
# If you excpect some code to return a Value
# and see None instead, something might be wrong
empty = None

"""
4/  the following syntax declares a function.

    functions are the building blocks of 
    more complex programs. 

    in the following exemple:
    'increment' is the function name
    'number' is an argument
    'return' is a special keyword used to make
    the function send back a result
"""


def increment(number):
    return number + 1


# here we call the function increment with the
# argument 9. the result of the function
# is assigned to the variable named ten
ten = increment(9)

# a common function is named print.
# It allows you to display text or a variable
print("Hello world!")

"""
5/  See how the increment function has its code
    shifted to the right with spaces? It means 
    the code lives inside a scope. Deeper from
    the global scope (no spaces).

    Everything inside is isolated. Variables declared
    inside a scope will cease to exist unless 
    you return them.

    Also, you can name them as you want without
    conflicting with other functions' scopes.

    It's like a little cosy space where stuff
    can happen, isolated from the outside world.

    From the outside it appears as a black box.

    From a given scope, you can always access things
    that exist in a parent scope, but never
    what's inside a deeper scope.
"""

"""
Your turn! Complete the exercises.

You'll have to change a variable
in each function named exerciseX
so it returns the correct answer.

Control your answers by running the unit tests.
"""


def exercise1():
    """
    change_me should return an integer.
    change the Value it is assigned
    """
    change_me = None
    return change_me


def exercise2():
    """
    change_me should return a float
    """
    change_me = None
    return change_me


def exercise3():
    """
    change_me should return a boolean
    """
    change_me = None
    return change_me


def exercise4():
    """
    change_me should return a string
    """
    change_me = None
    return change_me


def exercise5():
    """
    change the value assigned to the following
    variable so this function returns 5
    """
    change_me = 0
    return 4 + change_me


def exercise6(number):
    """
    change the value assigned to the following
    variable so this function returns
    always 0. Always
    """
    change_me = 99
    return number * change_me


def exercise7(number):
    """
    change the value so this function always
    returns a even number
    """
    change_me = 3
    return number * change_me
