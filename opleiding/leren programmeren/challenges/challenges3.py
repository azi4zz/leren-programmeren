lang = int(8) 
breed = int(3)
diep = float(1.5)
de_grootte = int(lang) * int(breed) * float(diep)
afvoeren = float(32.5)
afvoeren_prijs = float(de_grootte) * float(afvoeren)

uitgraven = int(25)
uitgraven_prijs = int(uitgraven) * float(de_grootte)

afstand = int(60)
voorrijkosten = 250 + (int(afstand) * 2.05)
totaal_prijs = uitgraven_prijs + afvoeren_prijs + voorrijkosten
print("uitgraven : €",uitgraven_prijs) 
print("afvoeren grond : €", afvoeren_prijs)
print("voorrijkosten : €" , voorrijkosten)
print("totaal : € " , totaal_prijs ) 
