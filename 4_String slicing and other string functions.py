a = "Harry is a good boy"
#Index of a string starts from 0 same like list
print(a[1])

#Slicing
#string[start:end:step]
print(a[1:5:2])

#Reverse a string
print(a[::-1])

#Length of string
print(len(a))

#split each element of string
print(list(a))

#split elements of list based on space or some character
print(a.split(" "))

#Check if string is alphanumeric
print(a.isalnum())

#Check if string is alpha
print(a.isalpha())

#Check if string is all uppercase
print(a.isupper())

#Check if string is all lowercase
print(a.islower())

#Convert first letter to capital
print(a.capitalize())

#Convert to uppercase
print(a.upper())

#Convert to lowercase
print(a.lower())

#check startswith
print(a.startswith("Har"))

#check endswith
print(a.endswith("Har"))

#check count
#Count is case sensitive
print(a.count("H"))

#Find in string
print(a.find("Har"))

#Replace in string
print(a.replace("Har", "Bar"))

