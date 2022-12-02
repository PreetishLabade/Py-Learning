# Function is used to reuse our code
# A good practice is to write a docstring for every function we define
# Docstring is nothing but a comment that describes the function

def func01():
    """This function prints that it is a function"""
    print("This is a function")


func01()

a = func01()
print(a)  # This output will be None because the func01 is not returing anything


# Hence, None is stored in a , which is printed

def func02(q,w):
    """This function gives sum of two numbers"""
    c = q+w
    return c

b = func02(10,12)
print(b)


#To read docstring of a function

print(func02.__doc__)