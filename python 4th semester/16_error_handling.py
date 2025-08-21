# Python Error Handling and Control Flow

## 1. try-else

# The `else` block runs **only if no exception** is raised in the `try` block.


try:
    num = int(input("Enter a number: "))
except ValueError:
    print("That's not a number!")
else:
    print("You entered:", num)


## 2. try-finally

# The `finally` block **always runs**, no matter if an exception occurs or not. Useful for cleanup actions.


try:
    print("Trying to open file")
    f = open("file.txt", "r")
except FileNotFoundError:
    print("File not found!")
finally:
    print("This will always run.")

## 3. raise (Raising Exceptions)

# Used to **manually throw** an exception when needed.


age = -1
if age < 0:
    raise ValueError("Age cannot be negative")


## 4. Exception

# An exception is an error that disrupts normal execution. You can handle it using `try-except` blocks.


try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")


## 5. match-case (Python 3.10+)

# Replaces switch-case. Used for checking multiple conditions.


command = "start"
match command:
    case "start":
        print("Starting")
    case "stop":
        print("Stopping")
    case _:
        print("Unknown command")


## 6. Common Exception Types

# | Exception         | When It Occurs                                |
# | ----------------- | --------------------------------------------- |
# | ZeroDivisionError | Dividing by zero                              |
# | ValueError        | Invalid value (e.g., converting "abc" to int) |
# | TypeError         | Wrong data type used                          |
# | IndexError        | Index out of range                            |
# | KeyError          | Accessing a non-existing dictionary key       |
# | FileNotFoundError | File does not exist                           |

## 7. try-except-finally (Full Example)


try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Can't divide by zero")
else:
    print("Result is:", result)
finally:
    print("Program finished")


## 8. Custom Exception

# You can create your own exception by subclassing `Exception`.


class MyError(Exception):
    pass

raise MyError("Something went wrong")

