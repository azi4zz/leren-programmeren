vraag1 = int(input("hoe duur is  de iphone ?"))
vraag2 = int(input("hoe duur is  de galaxy ?"))
verschil = vraag1 - vraag2
if verschil<50:
    print("de iphone is het duurst, de telefoon kost:",vraag1 )
    print("de galaxy is goedkoopst,de telefoon kost:" ,vraag2)
    print("het advies is dus de iphone te kopen .deze is namelijk" ,verschil, "duurder dan de galaxy.")
else:
    print("de verschil is meer dan 50")
    print("het advies is dus de galaxy te kopen .deze is namelijk goedkoper dan iphone")
