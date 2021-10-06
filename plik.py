x=2
while x>1:
    imie = input("podaj imie: ")
    if imie == "stop":
        break
    wiek = input("podaj wiek: ")
    print("witaj, ", imie , "-->", int(wiek) ** 2)

x =10
while x:
    x = x -  1
    if x % 2 != 0:
        continue
    print(x, end=' ')