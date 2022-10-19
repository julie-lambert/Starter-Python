import re

f = open("data.txt", "r")

regex = re.findall(r"\b[a-zA-Z]{1,}\b", f.read())

print(len(regex))
f.close()