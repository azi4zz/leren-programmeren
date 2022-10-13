lang = float(input("hoe lang is de zwembad?")) 
breed = float(input("hoe breed is de zwembad?"))
diep = float(input("hoe diep is de zwembad?"))

de_grootte = float(lang) * float(breed) * float(diep)
vierkante = float(lang) * float(breed) * 5 

afvoeren = float(32.5)
afvoeren_prijs = float(de_grootte) * float(afvoeren)

uitgraven = int(25)
uitgraven_prijs = int(uitgraven) * float(de_grootte)
afstand = float(input("hoe ver is de zwembad van het bedrijf?"))

if de_grootte > 20 and afstand > 50  :
    voorrijkosten = 250 + (int(afstand) * 2.05)

elif de_grootte > 20 and afstand < 50  :
    voorrijkosten = 250 + (int(afstand) * 2.15)

elif de_grootte < 20 and afstand > 50:
    voorrijkosten = 100 + (int(afstand) * 1.15)

elif de_grootte < 20 and afstand < 50:
    voorrijkosten = 100 + (int(afstand) * 1.25)

beton_kleur = input ("welke kleur wilt u het zwembad afwerken?wit/rood/andere")

if de_grootte > 20 and beton_kleur == "wit" :
    beton_prijs = float(vierkante) * 200

elif de_grootte < 20 and beton_kleur == "wit" :
    beton_prijs = float(vierkante) * 250

elif de_grootte > 20 and beton_kleur == "rood" :
    beton_prijs = float(vierkante) * 220

elif de_grootte < 20 and beton_kleur == "rood" :
    beton_prijs = float(vierkante) * 275

elif de_grootte > 20 and beton_kleur == "andere" :
    beton_prijs = float(vierkante) * 325

elif de_grootte < 20 and beton_kleur == "andere" :
    beton_prijs = float(vierkante) * 350

totaal_prijs = uitgraven_prijs + afvoeren_prijs + voorrijkosten  + beton_prijs

print("uitgraven : €",uitgraven_prijs) 
print("afvoeren grond : €", afvoeren_prijs)
print("voorrijkosten : €" , voorrijkosten)
print("beton + tegel : €" , beton_prijs)
print("totaal : € " , totaal_prijs ) 
