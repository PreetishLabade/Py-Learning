a = [1,2,5,4,7]

#Sort a list
#once a list is sorted, this change happens in the original list
a.sort(reverse=False)
print(a)

#Slicing in list is just like string slicing

#Slice list elements
print(a[0:4])

#Reverse a list
print(a[::-1])

#length of list
print(len(a))

#Min and max of list
print(min(a))
print(max(a))

#Append elements to list
#Append adds element in the end
a.append(9)
print(a)

#Insert element at an index position
a.insert(0, 88)
print(a)

#Remove element from list
a.remove(88)
print(a)

#List is mutable, ordered, duplicates allowed
#I can change any element of this list
a[0] = 25
print(a)

#Tuple is immutable, ordered, duplicates allowed
b = (1,2,4,5)
#b[0] = 5
print(b)

#Swap two numbers
y = 5
z = 6

y , z = z , y
print(y,z)