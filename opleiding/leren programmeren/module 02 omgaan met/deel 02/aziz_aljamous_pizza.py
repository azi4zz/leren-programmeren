pizzas = int(input("hoe veel pizza small wilt u?"))
pizzam = int(input("hoe veel pizza medium wilt u?"))
pizzal = int(input("hoe veel pizza large wilt u?"))
pizza_prijs_s = 6
pizaa_prijs_m = 8
pizza_prijs_L = 9
totaal_prijs = (pizza_prijs_s * pizzas ) + (pizaa_prijs_m * pizzam )+ (pizza_prijs_L * pizzal )

print  ("u heeft" , pizzas , "pizza small besteld " "en"  , pizzam , " pizza meduim "  "en" , pizzal , "pizza large besteld")
print ("wordt het", totaal_prijs, "euro")
print ("eet smakelijk alvast ")