aantal_personnen = int(input("hoe veel zijn jullie?")) 
gameseat_kost_voor_een_person_per_5min = 0.37
gameseat_kost_voor_een_person_per_1min = 0.37 / 5
tijd_spelen = int(input("hoe veel minuten willen jullie sppelen?"))
totaal_prijs = (gameseat_kost_voor_een_person_per_1min *  aantal_personnen * tijd_spelen) 
print ( "Dit geweldige dagje-uit met", aantal_personnen ,"mensen in de Speelhal met" ,tijd_spelen , "minuten VR kost je maar" ,totaal_prijs, "euro")
