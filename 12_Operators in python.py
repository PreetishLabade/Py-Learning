#Arithmetic operators
print(5+6)
print(5-6)
print(5*6)
print(5/6)
print(5//6)#Converts answer to int if it is float
print(5**6)#Shows 5^6
print(5%6)#Shows remainder

#Assignment operator
a = 5
print(a)

a = a+2
print(a)
#This can be written as a +=2

a -= 2
print(a)

a *= 2
print(a)

a %= 2
print(a)

a -= 2
print(a)

#Comparison operators
a = 2
if a == 5:
    print("True")
else:
    print("False")

#Above If condition can also be written as
print(a == 5) #Output will be false

#Logical operators
a = 1
b = 0
c = bool(a and b)
print(c)
c = bool(a or b)
print(c)
c = bool(a ^ b)#This is XOR
print(c)

#Identity operators
print(a is b)
print(a is not b)

#Membership operators
z = [1,2,3,4,5]
print(1 in z)
print(1 not in z)