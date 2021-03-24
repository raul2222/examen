#from manage_cinema import Cinema



def get_list(nombre_fichero):
    nombre = nombre_fichero
    f = open (nombre, "rt", encoding="utf-8")
    vacio = True
    for linea in f:
        print(linea)
        vacio = False
    
    if vacio == True:
        raise ValueError("Fichero vacio")

    return 0
    


f1 = get_list("palabras.txt")