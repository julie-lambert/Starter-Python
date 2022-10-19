#Longueur = L  Largeur = l

L = int(input("Veuillez saisir la valeur de L: "))
l = int(input("Veuillez saisir la valeur de l: "))

for i in range(1, L+1):
    print("|", end="")
    for j in range(1, l+1):
        if i == 1 or i == L:
            print("-", end="")
        else:
            print(" ", end="")
    print("|")
