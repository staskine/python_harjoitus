# Kirjoita ratkaisusi alle
# Käytössäsi on muuttujat:
# - kortti1, kortti2, maa1, maa2 (kaikki merkkijonotyyppisiä)
arvo1 = 0
arvo2 = 0

if kortti1 == "Ässä":
    arvo1 += 1
    arvo2 += 11
if kortti2 == "Ässä" and kortti1 != "Ässä":
    arvo1 += 1
    arvo2 += 11
if kortti1 == kortti2 and kortti1 == "Ässä":
    arvo1 = 2
    arvo2 = 12
if kortti1 == "2":
    arvo1 += 2
if kortti2 == "2":
    arvo1 += 2
if kortti1 == "3":
    arvo1 += 3
if kortti2 == "3":
    arvo1 += 3
if kortti1 == "4":
    arvo1 += 4
if kortti2 == "4":
    arvo1 += 4
if kortti1 == "5":
    arvo1 += 5
if kortti2 == "5":
    arvo1 += 5
if kortti1 == "6":
    arvo1 += 6
if kortti2 == "6":
    arvo1 += 6
if kortti1 == "7":
    arvo1 += 7
if kortti2 == "7":
    arvo1 += 7
if kortti1 == "8":
    arvo1 += 8
if kortti2 == "8":
    arvo1 += 8
if kortti1 == "9":
    arvo1 += 9
if kortti2 == "9":
    arvo1 += 9
if kortti1 == "10":
    arvo1 += 10
if kortti2 == "10":
    arvo1 += 10
if kortti1 == "Jätkä":
    arvo1 += 10
if kortti2 == "Jätkä":
    arvo1 += 10
if kortti1 == "Kuningatar":
    arvo1 += 10
if kortti2 == "Kuningatar":
    arvo1 += 10
if kortti1 == "Kuningas":
    arvo1 += 10
if kortti2 == "Kuningas":
    arvo1 += 10



#tulostus
print(maa1, kortti1)
print(maa2, kortti2)
if arvo2 == 0:
    print("Yhteensä:", str(arvo1))
else:
    arvo2 = arvo1 + 10
    print(f"Yhteensä: {str(arvo1)} tai {str(arvo2)}")
    
if arvo1 == 21 or arvo2 == 21:
    print("BLACKJACK")






    


