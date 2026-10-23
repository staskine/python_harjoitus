x = 0
y = 0
tulos = 0
loppuuko = "e"

while 1:
    x = input("Laita eka numero:")
    y = input("Laitapa se toinenkin:")
    tulos = int(x) + int(y)
    print(f"Eka: {str(x)}  Toka: {str(y)}  Tulos: {tulos}")
    loppuuko = input("Ootko valmis? E vai J?")
    if loppuuko == "J":
        break