print("mijn game gaat over dat je in bos bent en je wilt  uitgaan,")
print("maar moeten de dieren jou laten gaan of moet je oplossing vinden")
naam = input("wat is uw naam?")
rechting = input("In welke rechting ga je lopen? noord/west/oost/zuid ")
if rechting == "zuid":
     aap = input("wat geef je de aap? banaan/ klaver ")
     if aap == "banaan":
        print("mooi naar volgende stap.")
        aantal_km = int(input("hoeveel km zou je rennen ?"))
        if aantal_km <= 5 :
            minder = input("Wat pak je op voor  de schaap?mes/eten ")
            if minder == "eten":
                print("goed gedaan")
                eten = input("wat pak je op voor de konijn? wortels / pataat ")
                if eten == "wortels":
                    print("mooi ja bent nu buiten het bos, gefeliciteerd ", naam,)
                elif eten == "pataat":
                    print("sorry je kunt niet doorgaan")    
            elif minder == "mes":
                print("Schreeuwen, je bent klaar.")
        elif aantal_km < 10:
            eenkhoorn = input("wat pak je op voor de eenkhoorn?gras/noten ")
            if eenkhoorn == "noten":
                print(f"Wat een intelligentie gefeliciteerd {naam}")
        else:
            kat = input("wat pak je op voor kat ? yoghurt/ noten ")
            if kat == "yoghurt":
                print(f"mooi ja bent nu buiten het bos, gefeliciteerd {naam}")
            elif kat == "noten":
                print("game over de kat eet geen noten")  
     if aap == "klaver":
        print("game over ):")

if rechting == "oost":
   konijn = input("wat pak je op voor de konijn? wortels / pataat")
   if konijn == "wortels":
        print("perfect u kunt doorgaan ")
        aantal_km = int(input("hoeveel km zou je rennen ?"))
        if aantal_km <= 5 :
            minder = input("Wat pak je op voor  de schaap?mes/eten")
            if minder == "eten":
                print("goed gedaan")
                eten = input("wat pak je op voor de konijn? wortels / pataat")
                if eten == "wortels":
                    print("mooi ja bent nu buiten het bos, gefeliciteerd ", naam,)
                elif eten == "pataat":
                    print("sorry je kunt niet doorgaan")    
            elif minder == "mes":
                print("Schreeuwen, je bent klaar.")
        elif  aantal_km < 10:
            eenkhoorn = input("wat pak je op voor de eenkhoorn?gras/noten")
            if eenkhoorn == "noten":
                print(f"Wat een intelligentie gefeliciteerd {naam}")
        else:
            kat = input("wat pak je op voor kat ? yoghurt/ noten")
            if kat == "yoghurt":
                print(f"mooi ja bent nu buiten het bos, gefeliciteerd {naam}")
            elif kat == "noten":
                print("game over de kat eet geen noten")  
   elif konijn == "pataat":
        print("game over ):")





 
if rechting == "west":
     schild = input("wat ga je doen als je schildpad ziet? vechten/ rennen")
     if schild == "vechten":
        print("mooi naar volgende stap.")
        aantal_km = int(input("hoeveel km zou je rennen ?"))
        if aantal_km <= 5 :
            minder = input("Wat pak je op voor  de schaap?mes/eten")
            if minder == "eten":
                print("goed gedaan")
                eten = input("wat pak je op voor de konijn? wortels / pataat")
                if eten == "wortels":
                    print("mooi ja bent nu buiten het bos, gefeliciteerd ", naam,)
                elif eten == "pataat":
                    print("sorry je kunt niet doorgaan")    
            elif minder == "mes":
                print("Schreeuwen, je bent klaar.")
        elif  aantal_km < 10:
            eenkhoorn = input("wat pak je op voor de eenkhoorn?gras/noten ")
            if eenkhoorn == "noten":
                print(f"Wat een intelligentie gefeliciteerd {naam}")
        else :
            kat = input("wat pak je op voor kat ? yoghurt/ noten ")
            if kat == "yoghurt":
                print(f"mooi ja bent nu buiten het bos, gefeliciteerd {naam}")
            elif kat == "noten":
                print("game over de kat eet geen noten")  
     if schild == "vechten":
        print("game over de schild zo sterk")
if rechting == "noord":
     hond = input("wat ga je doen als je hond ziet? temmen/rennen ")
     if hond == "temmen":
        print("mooi naar volgende stap.")
        aantal_km = int(input("hoeveel km zou je rennen ?"))
        if aantal_km <= 5 :
            minder = input("Wat pak je op voor  de schaap?mes/eten")
            if minder == "eten":
                print("goed gedaan")
                eten = input("wat pak je op voor de konijn? wortels / pataat")
                if eten == "wortels":
                    print("mooi ja bent nu buiten het bos, gefeliciteerd ", naam,)
                elif eten == "pataat":
                    print("sorry je kunt niet doorgaan")    
            elif minder == "mes":
                print("Schreeuwen, je bent klaar.")
        elif  aantal_km < 10:
            eenkhoorn = input("wat pak je op voor de eenkhoorn?gras/noten")
            if eenkhoorn == "noten":
                print(f"Wat een intelligentie gefeliciteerd {naam}")
        else:
            kat = input("wat pak je op voor kat ? yoghurt/ noten")
            if kat == "yoghurt":
                print(f"mooi ja bent nu buiten het bos, gefeliciteerd {naam}")
            elif kat == "noten":
                print("game over de kat eet geen noten")  
     if hond == "rennen":
        print("je bent dood gegaan game over ):")