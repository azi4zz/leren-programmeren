n = 0
while n == 0 :
    try:
        pizzas = int(input("hoe veel pizza small wilt u?"))
        n += 1 
    except : print("vul getaal in")

while n== 1:
    try:
      pizzam = int(input("hoe veel pizza medium wilt u?"))
      n+= 1
    except :print("vul getaal in") 

while n == 2:
    try:
        pizzal = int(input("hoe veel pizza large wilt u?"))
        n+=1
    except:print("vul getaal in")    
pizza_prijs_s = 6
pizaa_prijs_m = 8
pizza_prijs_L = 9
totaal_prijs = int(pizza_prijs_s * pizzas ) + int(pizaa_prijs_m * pizzam )+ int(pizza_prijs_L * pizzal )

print  ("u heeft" , pizzas , "pizza small besteld en"  , pizzam , " pizza meduim en" , pizzal , "pizza large besteld")
print ("wordt het", totaal_prijs, "euro")
print ("eet smakelijk alvast ")