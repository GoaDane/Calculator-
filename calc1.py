import math

def add(x, y):
    return(x+y)

def subtract(x, y):
    return(x-y)
    
print("Your option: ")
print("1 to add")
print("2 to subtract")

action = int(input("What do you want to do?: " ))

x = int(input("Gimme the first number: "))
y = int(input("Gimme the second number: "))

if(action == 1):
    result = add(x, y)
elif(action == 2):
    result = subtract(x, y)

print("The result is: ", result)
