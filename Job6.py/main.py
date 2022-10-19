x = input("> ")


while not x == "Bonjour":
    print(x)
    x = input("> ")

    if x == "Bonjour":
         print("Bonjour à toi!")
         x = input("> ")

    if x == "Au revoir":
        break
