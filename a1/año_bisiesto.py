anio = 2000
def es_bisiesto():
    global anio
    if anio % 4 ==0:
        if anio % 100 ==0:
            if anio % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False    
if es_bisiesto():
    print(f"{anio} es bisiesto")
