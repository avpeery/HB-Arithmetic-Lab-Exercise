"""Math functions for calculator."""


def add(num1, num2):
    """Return the sum of the two inputs."""
    return num1+num2

def subtract(num1, num2):
    """Return the second number subtracted from the first."""
    return num2 - num1

def multiply(num1, num2):
    """Multiply the two inputs together."""
    return num1*num2

def divide(num1, num2):
    """Divide the first input by the second and return the result."""
    return num1/num2

def square(num1):
    """Return the square of the input."""
    return num1**2

def cube(num1):
    """Return the cube of the input."""
    return num1**3

def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    return num1**num2

def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    return num1 % num2

def complicated_calculation(num1, num2, num3):
    return ((num1 + num2) * num3)


def turn_str_into_int(l):
    """takes list and turns string numbers into integers"""
    new_list = []
    for item in l:
        if item.isdigit():
            new_list.append(int(item))
        else:
            new_list.append(item)
    return new_list

print("Welcome the arithmetic calculator!")
while True:
    user_input = input("What is your calculation? Please enter the operator first, followed by the numbers. Leave spaces between your entries. > ")
    user_input = turn_str_into_int(user_input.split(" "))

    print(user_input)

    if user_input[0] == "+":
        print(add(user_input[1], user_input[2]))
    elif user_input[0] == "-":
        print(subtract(user_input[1], user_input[2]))
    elif user_input[0] == "*":
        print(multiply(user_input[1], user_input[2]))
    elif user_input[0] == "/":
        print(divide(user_input[1], user_input[2]))
    elif user_input[0] == "**" and user_input[2] == 2 or user_input[0] == "squares":
        print(square(user_input[1]))
    elif user_input[0] == "**" and user_input[2] == 3 or user_input[0] == "cubes":
        print(cube(user_input[1]))
    elif user_input[0] == "**" and not user_input[2] == 2 and not user_input[2] == 3:
        print(power(user_input[1], user_input[2]))
    elif user_input[0] == "%":
        print(mod(user_input[1], user_input[2]))
    else:
        print("Sorry cannot compute! Try again.")

    continue_game = input("Would you like to play again?")
    if continue_game.upper() == "NO":
        print("Goodbye!")
        break

#greeting function (welcomes greeter)
#turns string numbers in list to integers
#basic operator functions
#play calculator function
#continue game function
#