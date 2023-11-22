
"""
Explain the difference between a list and tuple in Python?

1. List and Tuples are sequential data types to store collection of objects.
2. Lists are represented as square brackets and Tuples are represented with parantheses.

 Difference: 
    Lists are mutable and tuples are immutable. It means lists can be modified, appended or sliced but tuples cannot be modfied.
 

How to handle exceptions in Python ?

    In Python, exceptions are used to handle any run time error during the execution of the program.
    It prevents the program from crashing. 
    The basic structure for handling exceptions in Python involves the use of try, except, else, and finally blocks.


What is a virtual environment in Python used for?

Virtual environment in python is used to create an isolated environment for the project. It helps to manage dependencies,
ensuring the packages installed for one project doesn't hinder or interfere with another project.

In MacOs and Linux, virtual environment is created by running

    python3 -m venv venv
    source venv/bin/activate


Explain the concept of a decorator in Python?

    They are essentially functions that add functionality to an existing function without changing the structure of 
    the function itself. They are represented as @decorator_name and called in bottom up fashion

Describe what a generator function is and how it differs from a regular function?

    Generator functions return an iterable collection of items, one at a time, in a set manner. 

    1. Generator employ the use of yield keyword rather than return to return a generator function.
    2. Generator functions maintains its state, which can be memory efficient when generating large sequences of values,
    as only  one value needs to be kept in memory at a time.
    3. Generator functions keeps its state between calls, allowing it to resume execution from the last yield statement. However,
        normal function runs from start to finish

"""

class carGurus:
    def __init__(self, demoList, demoTuple):
        self.demoList = demoList
        self.demoTuple = demoTuple
    
    def listFunction(self, value, position):
        print(" Print demo List before change", self.demoList)
        if  position >= 0 and position < len(self.demoList) :
         self.demoList[position] = value
        print(" Print demo List after change", self.demoList)
    
    def tupleFunction(self, value, position):
        print(" Print demo Tuple before change", self.demoTuple)
        if position >= 0 and position < len(self.demoTuple) :
#Exception raised because tuples are immutable and 'tuple' object does not support item assignment.
            try:
                self.demoTuple[position] = value
            except Exception as e:
                print(" Exception " , e)
            finally:
                pass
        print(" Print demo Tuple after change", self.demoTuple)


    def generatorFunction(self):
        num = 0
        while num < len(self.demoList):
            yield self.demoList[num]
            num += 1
    
    def generatorExpression(self):
        listGenerated = (self.demoList[i] for i in range(len(self.demoList)))
        print(listGenerated)


#Decorator functions

def goodMorning(functionName):
    def wrapper( name):
        message = "Good Morning " + name.capitalize() 
        message_morning = functionName(message)
        return message_morning
    return wrapper

@goodMorning
def messaging(name):
    return name


if __name__ == "__main__":
    demoList = [1, 2, 3, 4, 5]
    demoTuple = (1, 2, 3, 4, 5)
  #Create a class object
    objCarGurus = carGurus(demoList,demoTuple)
  #Call the functions to check the difference
    objCarGurus.listFunction(8,2)
    objCarGurus.tupleFunction(8,2)
  #Generator function and expression
    objCarGurus.generatorFunction()
    objCarGurus.generatorExpression()
  # Decorator function call
    print(messaging("cargurus"))
    
