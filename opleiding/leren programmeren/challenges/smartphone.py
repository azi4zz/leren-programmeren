iphone_prijs = int(input("hoe duur is  de iphone ?"))
galaxy_prijs = int(input("hoe duur is  de galaxy ?"))
verschil = iphone_prijs - galaxy_prijs
if galaxy_prijs> iphone_prijs:
    print("het advies is dus de iphone te kopen want galaxy is duruder")
if  verschil>50:
    print("de iphone is het duurst, de telefoon kost:",iphone_prijs )
    print("de galaxy is goedkoopst,de telefoon kost:" ,vraag2)
    print("het advies is dus de iphone te kopen .deze is namelijk" ,verschil, "duurder dan de galaxy.")
else:
    print("de verschil is meer dan 50")
    print("het advies is dus de galaxy te kopen .deze is namelijk goedkoper dan iphone")
