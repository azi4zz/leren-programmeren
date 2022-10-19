a = int(input("geef een getal:"))
b = int(input("geef een getal:"))

if a > b :
    max = a
    min = b
    print (f"a is het grootste getal : {max}")
    
elif a < b : 
    min = a
    max = a
    print(f"b is het grootste getal : {min}")

else :
    print(f"a en b zijn even groot ")
    