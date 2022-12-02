"""Try except is used to handle exceptions
Write a code to accept inputs from user and print sum
Handle the situation with an error message when user inputs a string as input"""
try:
    a = float(input("Enter a number"))
    b = float(input("Enter another number"))
    print("Sum of the two numbers is", a + b)

except Exception as e:
    print("Please enter a valid input. Acceptable input is numbers only")