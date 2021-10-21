
"""
Chapter 2

In the previous chapter, we learned about variables.
We can assign values of different types and use operators.

Now let's devine on flow control!
"""

"""
1/  Conditions allow you to branch
    on multiple code paths.

    you start with the keyword 'if' then evaluate 
    a boolean condition. 
    E.g. "Hey, wanna eat something?" could be answerd yes or no.
    In programming: True or False

    You can prepare an alternative path if the condition is false
    with the 'else' keyword

    Note: code inside an if/else statement is scoped like in functions.
"""


hungry = False

if hungry == True:
    print("you should eat")
    # since the variable if False
    # there is no way the code gets here
else:
    print("let's take a walk")


"""
a condition is a boolean expression
it can be directly a boolean variable,
or the result of comparison operators.
Equal       ==
Not Equal   !=
Less        <
Greater     >
            and
            or
            not
"""

# in the following example, we have more than 
# one condition. They are evaluated sequentially.
age = 5

if age < 12:
    print("you are a kid")
elif age < 18:
    print("you are a teen")
else:
    print("you are an adult")

"""
2/  Loops allow to repeat multiple times a set of
    instructions. 

    In the following example, we use a while loop.
    As long as the condition is met, the loop is 
    going to repeat.
"""

# Let's fill this coffee cup
cup_ml = 0
coffee_cup_full = False

while coffee_cup_full == False:
    print("filling coffee")

    cup_ml = cup_ml + 10
    if cup_ml >= 110:
        coffee_cup_full = True

"""
3/  For loops are very similar to while loops.
    They offer a different approach to problems
    based on steps.
"""

# this loop will print numbers from 1 to 10
# range is a function that returns numbers
# sequentially from 0 up to the target number
# with steps of 1
for x in range(10):
    print(x + 1)

# this code is identical to the example
# with the while loop above
for x in range(0, 110, 10):
    print("filling coffee")


"""
Your turn! Complete the exercises.

You'll have to change a variable
in each function named exerciseX
so it returns the correct answer.

Control your answers by running the unit tests.
"""

def exercise1(number):
    """
    complete the following code
    """
    sum = 1
    for i in range(10):
        sum += 1

    return sum

def exercise2(text):
    """
    complete the following code.
    Fill result with the content of the argument text inverted.

    Lowercase letters should be uppercase.
    Uppercase letters should be lowercase.

    tip: use .capitalize() or .lower() to make letters upper or lower case.
    tip: you may use isupper() and islower() as conditions.
    
    """
    result = ""
    for letter in text:        
        if letter.isupper():
            result += letter.lower()

    return result