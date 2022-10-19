def myFunction(*args):

    myList = [*args]

    for x in myList:
        if x % 2 == 0:
            print(x)

myFunction(1,2,10,25,32,44,47,49,54,63)