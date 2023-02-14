 aantal_croissantjes = int(input("hoe veel croissantjes wilt u hebben? "))
croissantjes_prijs = 0.39
aantal_stokbroden = int(input("hoe veel stokbroden wilt u hebben?"))
stokbroden_prijs = 2.78
aantal_kortingsbonnen = int(input("joe veel kortingsbonnen heeft u?"))
kortingsbonnen = 0.50
prijs =(aantal_croissantjes * croissantjes_prijs + aantal_stokbroden * stokbroden_prijs - kortingsbonnen * aantal_kortingsbonnen) 
print  ( "de feestlunch prijs =", prijs, "euro voor de " , aantal_croissantjes ,"en de"  ,aantal_stokbroden, "stokbroden als de " , aantal_kortingsbonnen, "kortingsbonnen nog geldig zijn")