x = 0
y = 0
tulos = 0
loppuuko = "e"

while 1:
    x = input("Laita eka numero:")
    y = input("Laitapa se toinenkin:")
    tulos = int(x) + int(y)
    tulo = int(x) * int(y)
    kerto = input("Kerrotaanko se nyt samalla? k = kyllä:  ")
    print(f"Eka: {str(x)}  Toka: {str(y)}\nTulos: {tulos}")
    if kerto == "k":
        print("Tulo:", str(tulo))
    loppuuko = input("Ootko valmis? E vai J?: ")
    if loppuuko == "J":
        print("Kiva kun käytit tätä")
        break