import re

nbr = int(input("Entrez un nombre: "))

f = open("data.txt", "r")

regex = re.findall(r"\b[a-zA-Z]{%d}\b" %(nbr), f.read())

print(f"Il y a {len(regex)} mots de {nbr} caractères")
