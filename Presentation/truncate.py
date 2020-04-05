f = open("Presentation/example.txt", "a")
print(f.truncate(10))
f.close()
f = open("Presentation/example.txt", "r")
print(f.read())

