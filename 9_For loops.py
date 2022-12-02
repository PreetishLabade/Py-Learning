#General for loop
a = ["a","b","c","d"]
for i in a:
    print(i)

#Nested list for loop
b = [["a",1],["b",2],["c",3],["d",4]]
for x,y in b:
    print(x,y)

#If condition in for loop
for k,l in b:
    if l < 3:
        print(k)

#From given list, print numbers gretaer than 6
x = ["a",5,6,2,7]
for i in x:
    if type(i) == int:
        if i > 6:
            print(i)