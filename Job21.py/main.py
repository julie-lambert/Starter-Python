def mySort(*args):
    args = list(args)
    r = []
    while args:
        mini = args[0]
        for x in args:
            if x < mini:
                mini = x
        args.remove(mini)
        r.append(mini)
    return r

def myDisplay(mySort):
    print(myDisplay)


myDisplay(mysort[17,7,12,1,12,4,18,1])
