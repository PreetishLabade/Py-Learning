#Set is Mutable, unordered and no duplicates are allowed
a = [1,2,3,4,4]
b = set(a)
print(b)

#Create a set
a = set()

#Add elements to set
a.add(1)
a.add(2)
print(a)

#Remove elements from set
a.remove(1)
print(a)

#Check intersection
b = {1,2}
print(a.intersection(b))

#Check union
print(a.union(b))