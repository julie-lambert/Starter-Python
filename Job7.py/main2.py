a = 3
b = 5

for i in range(0, 100 + 1):
    s = ""

    if (i == a):
        a = a + 3
        s = s + "Fizz"
    if (i == b):
        b = b + 5
        s = s + "Buzz"
    if (s == ""):
        print(i)
    else:
        print(s)
#