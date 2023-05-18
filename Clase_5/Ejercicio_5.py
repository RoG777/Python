def bisiesto():

    bisiesto = (int(input("ingresa un año: ")))
        
    if bisiesto % 4 == 0 and (bisiesto % 100!= 0 or bisiesto % 400 == 0):
        print("Es bisiesto") 
        
    else:
        print("No es bisiesto")

bisiesto()
















