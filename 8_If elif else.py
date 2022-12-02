print("Please enter your age")
age = int(input())

if age > 18:
    print("Congrats! You are eligible to drive")
elif age == 18:
    print("You need to pass a test before you can drive")
else:
    print("Sorry! You are not eligible to drive")