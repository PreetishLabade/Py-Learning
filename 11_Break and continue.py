a = 0

while a<10:
    print(a, end=" ")
    a = a+1

#Break-breaks the loop and comes out of it
#Continue-Continue executing the same loop

#Accept input from user
#If input is less than 100, then take no action and ask for input again
#when input is more than 100, print the input

a = int(input("Please enter a number" ))

while(True):
    if a < 100:
        a = int(input("Please enter a number" ))
        continue
    else:
        print(a)
        break