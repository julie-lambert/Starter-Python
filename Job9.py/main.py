n = int(input("Saisir la hauteur du triangle: "))

for i in range(1, n+1):
    for j in range(1, n+1):
        if j == n-i+1 or j == n+i-1:
            print("/", end="")
        elif i == n:
            print("_", end="")
        else:
            print("",end="")
    print()