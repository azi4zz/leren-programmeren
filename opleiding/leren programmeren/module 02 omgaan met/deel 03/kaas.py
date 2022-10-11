kaas = input("is de kaas geel?")
if kaas == "ja" :
    gaten = input("zitten er gaten in?")
    if gaten == "ja" :
        belagelijk = input("is de kaas belagelijk duur?")
        if belagelijk == "ja" : 
            print("emmenthaler")
        if belagelijk == "nee" :
            print("leerdammer") 
    if gaten == "nee" : 
        hard = input("is de kaas hard als steen?")
        if hard == "ja" :
            print("parmigiano")
        if hard == "nee" :
            print("goudse kaas")

if kaas == "nee" : 
    schimmel = input("heeft de kaas blauwe schimmel?")
    if schimmel == "ja" : 
        korst = input("heeft de kaas een korst?")
        if korst == "ja" : 
            print("blue de rochbaron")
        if korst == "nee" : 
            print("foume d'ambert ") 
    if schimmel == "nee" :
        k = input("heeft de kaas een korst?")
        if k == "ja" :
            print("camembert")
        if k == "nee" :
            print("mozzarella")    

       
