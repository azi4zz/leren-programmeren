kaas = input("is de kaas geel?")
if kaas == "ja" :
    gaten = input("zitten er gaten in?")
    if gaten == "ja" :
        belagelijk = input("is de kaas belagelijk duur?")
        if belagelijk == "ja" : 
            print("emmenthaler")
        else :
            print("leerdammer") 
    else : 
        hard = input("is de kaas hard als steen?")
        if hard == "ja" :
            print("parmigiano")
        else:
            print("goudse kaas")

if kaas == "nee" : 
    schimmel = input("heeft de kaas blauwe schimmel?")
    if schimmel == "ja" : 
        korst = input("heeft de kaas een korst?")
        if korst == "ja" : 
            print("blue de rochbaron")
        else: 
            print("foume d'ambert ") 
    if schimmel == "nee" :
        k = input("heeft de kaas een korst?")
        if k == "ja" :
            print("camembert")
        else :
            print("mozzarella")    

       
