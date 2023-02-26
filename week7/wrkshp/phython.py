def greet(name):
    #this function prints a greeting to 
    print("hello," +name+ "!")
    #calling the function....below..
greet("John")

def greet(name):
    print("how are you," +name+ "!")
greet("alan shah")


def add(x,y):
    #This function adds two numbers and returns the result
    result=x+y
    return result

sum = add(3,4)
print(sum)

def add(x,y):
    result=x+y
    return result

sum = add(5,7) 
print(sum)

#Docstrings
def greet(alan):
    #The function takes as an argument and prints a greeting message to the console
print(f"Hello, {alan}!")
print(greet.doc)