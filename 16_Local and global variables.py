#Global and local variable
a = 10 # This is a global variable
print("This is a global variable", a)

def func01():
    a = 5 # This is a local variable
    return print("This is a local variable", a)

func01()

# Only global variable
b = 10 # This is a global variable

# If local varibale is not present, function will use global variable
def func02():
    return print(b)

func02()


# A function can only read a global variable. It cannot modify it
#Below func03 will generate an error message

c = 2 # This is a global variable

def func03():
    c = c + 1
    return print(c)

#func03()

# A function can modify a global variable when we use "global" keyword before it
print("Value before changing using global keyword ", c)
def func04():
     global c
     c = c + 1
     print("Value after changing using global keyword",c)

func04()

