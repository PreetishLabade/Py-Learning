#Dictionary
a = {"A":"Apple", "B":"Ball", "C":"Cat"}

#There is no indexing in Dictionary like Lists.
#There are key value pairs
#We can access values with keys as below
print(a["A"])

#Dictionary in dictionary
#A value of a key value pair in a dictionary can be a List, Dictionary or a tuple
a = {"A":"Apple", "B":"Ball", "C":"Cat", "D":{"D1":"Dog", "D2":"Don"}}
print(a["D"])

print(a["D"]["D1"])

#A key in a dictioanry is immutable. Value is mutable
a["A"] = "Another Apple"
print(a)

#Add elements to dictionary
a["E"] = "Elephant"
print((a))

#Delete elements from dictionary
del a["E"]
print(a)

#Create a copy of dictionary
b = a.copy()
print(b)

#Print only keys
print(a.keys())

#Print only values
print(a.values())

#Accept an input from user and output a value for that Key
print("Enter an alphabet")
c = input()
print(a[c])



