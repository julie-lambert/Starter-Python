texte = input("Entrez votre texte: ")

f = open("output.txt", "a")
f.write(texte)
f.close()

f = open("output.txt", "r")

print(f.read())