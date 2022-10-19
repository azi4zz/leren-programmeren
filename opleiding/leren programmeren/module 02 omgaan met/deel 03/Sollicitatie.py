print("er wordt u een aantel relevante vragen gesteld ...")
print("gelieve die naar eer en geweten in tu vullen")
print("als blijkt dat u aan de criteria voldoet dan komt u in aanmerking voor een serirus sollicitatiegesprek")
print("ontspan maar blijf wakker, hier komen  de vragen")

Naam = input("wat is jou naam?")
diploma = input("heb je een Diploma MBO-4 ondernemen?")
rijbewijs = input("heb je  een geldig Vrachtwagen rijbewijs?")
hoed = input ("Ben je  in bezit van een hoge hoed?")
praktijk = int(input("Hoeveel jaar heb je praktijkervaring met dieren-dressuur?"))
praktijk1 = int(input("hoeveel jaar heb je praktijkervaring met jongleren?"))
praktijk2 = int(input("hoeveel jaar heb je prakrijkervaring metacrobatiek?"))
m = input("ben je een man of vrouw?")
if m == "man" :
    snoor = input("heb je een snoor?")
    if snoor == "ja" :
         snorLengte = int(input("Hoelang is uw snor? (in cm)"))
elif m == "vrouw" :
    haar = input("heb je  rood krullend haar? ")
    if haar == "ja":
        haarLengte = int(input("Hoelang is jou rood krullend haar? (in cm)"))
        
lengte = int(input ("Wat is jou lengte? (in cm)"))
gewicht = int(input ("Wat is jou gewicht? (in kg)"))      
if (praktijk > 4 or praktijk1 > 5 or praktijk2 > 3 ) and (diploma == "ja") and rijbewijs == "ja" and hoed == "ja" and ((m == "vrouw" and haar == "ja" and  haarLengte > 20) or (m == "man" and snoor == "ja"  and snorLengte > 10)) and (lengte > 150 and gewicht > 90):
    print ("Gefeliciteerd ", Naam    ,"! U komt in aanmerking voor een sollicitatiegesprek, stuur snel uw CV!")
else :
    print (" sorry " , Naam , "U voldoet niet aan onze strenge eisen voor de functie van Circusdirecteur, het spijt ons!")   


