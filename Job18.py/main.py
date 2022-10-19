def myFunction(*args):
    myList = [*args]
    myList.sort()
    print(myList)

myFunction(2, 6, 3, 10, 8)