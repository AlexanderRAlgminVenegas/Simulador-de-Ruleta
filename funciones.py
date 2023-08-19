from random import randint as r

rojos = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
negros = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
docena_1 = [1,2,3,4,5,6,7,8,9,10,11,12]
docena_2 = [13,14,15,16,17,18,19,20,21,22,23,24]
docena_3 = [25,26,27,28,29,30,31,32,33,34,35,36]
columna_1 = [1,4,7,10,13,16,19,22,25,28,31,34]
columna_2 = [2,5,8,11,14,17,20,23,26,29,32,35]
columna_3 = [3,6,9,12,15,18,21,24,27,30,33,36]

def sort1(lista):
    if lista:
        return sorted(lista)
    else:
        return []

def gen_cuadro(idx,columna):
    """Devuelve todas las combinaciones cuadro de columna[indice]
    SOLO SIRVE PARA LAS columnaS 1 Y 3"""
    try:
        if columna == "columna_1":
            if columna_1[idx] == 1:
                cuadros = [[1,2,4,5]]
            elif columna_1[idx] == 34:
                cuadros = [[31,32,34,35]]
            else:
                cuadros = [sort1([columna_1[idx-1],columna_2[idx-1],columna_1[idx],columna_2[idx]]),
                    sort1([columna_1[idx],columna_2[idx],columna_1[idx+1],columna_2[idx+1]])]
        elif columna == "columna_3":
            if columna_3[idx] == 3:
                cuadros = [[2,3,5,6]]
            elif columna_3[idx] == 36:
                cuadros = [[32,33,35,36]]
            else:
                cuadros = [sort1([columna_3[idx-1],columna_2[idx-1],columna_3[idx],columna_2[idx]]),
                    sort1([columna_3[idx],columna_2[idx],columna_3[idx+1],columna_2[idx+1]])]
    except IndexError:
        print("Error Cuadro")
    else:
        return(cuadros)
    
def gen_caballo(idx,columna):
    """Devuelve todas las combinaciones caballo de columna[indice]
    SOLO SIRVE PARA LAS columnaS 1 Y 3"""
    try:
        if columna == "columna_1":
            if columna_1[idx] == 1:
                caballo = [[1,2],[1,4]]
            elif columna_1[idx] == 34:
                caballo = [[31,34],[34,35]]
            else:
                caballo = [sort1([columna_1[idx-1],columna_1[idx]]),sort1([columna_1[idx],columna_2[idx]]),sort1([columna_1[idx],columna_1[idx+1]])]
        if columna == "columna_2":
            if columna_2[idx] == 2:
                caballo = [[1,2],[2,5],[2,3]]
            elif columna_2[idx] == 35:
                caballo = [[32,35],[34,35],[35,36]]
            else:
                caballo = [sort1([columna_2[idx-1],columna_2[idx]]),sort1([columna_2[idx],columna_2[idx+1]]),
                           sort1([columna_1[idx],columna_2[idx]]),sort1([columna_2[idx],columna_3[idx]])]
        if columna == "columna_3":
            if columna_3[idx] == 3:
                caballo = [[2,3],[3,6]]
            elif columna_3[idx] == 36:
                caballo = [[33,36],[35,36]]
            else:
                caballo = [sort1([columna_3[idx-1],columna_3[idx]]),sort1([columna_3[idx],columna_2[idx]]),sort1([columna_3[idx],columna_3[idx+1]])]
    except IndexError:
        print("Error columna")
    else:
        return(caballo)
            
def comprobar_apuesta(apuesta,cantidad_a,pos_ganadoras):
    ganancias = []
    perdidas = []
    for key in apuesta.keys():
        key_a = key + "_a"
        if cantidad_a[key_a]:
            for k in apuesta[key]:
                idx = list(apuesta.keys()).index(key)
                idx_k = apuesta[key].index(k)
                if k != "par":
                    if k in pos_ganadoras[idx]:
                        i = cantidad_a[key_a][idx_k]
                        ganancia = apuesta_ganada(key,i)
                        ganancias.append(ganancia)
                        print("Ha ganado " + str(ganancia) + " por la siguiente apuesta: " + key + ", ", k)
                    else:
                        i = cantidad_a[key_a][idx_k]
                        perdidas.append(i)
                else:
                    if pos_ganadoras[idx] == "par":
                        i = cantidad_a[key_a][idx_k]
                        ganancia = apuesta_ganada(key,i)
                        ganancias.append(ganancia)
                        print("Ha ganado " + str(ganancia) + " por la siguiente apuesta: " + key + ", ", k)
                    else:
                        i = cantidad_a[key_a][idx_k]
                        perdidas.append(i)
    return ganancias, perdidas

def apuesta_ganada(key,i):
    if key == "pleno":
        return 35*i
    elif key == "caballos":
        return 17*i
    elif key == "transversal":
        return 11*i
    elif key == "cuadros":
        return 8*i
    elif key == "seisena":
        return 5*i
    elif key == "columna":
        return 2*i
    elif key == "docena":
        return 2*i
    elif key == "color":
        return i
    elif key == "paridad":
        return i
    elif key == "falta_pasa":
        return i

class Ruleta():
    """Simula una ruleta europea"""
    
    def __init__(self):
        """Registrar la apuesta"""
        tir = r(0,36) # EL NUMERO ALEATORIO ENTRE 0 Y 36 QUE SALE DE LA RULETA
        self.tir = tir

    def tirada(self):
        """La función simula una tirada en la ruleta, sale un número entre el 0 y el 36.
        Devuelve el numero y las posibles combinaciones ganadoras. """
        t = self.tir
    
        # FALTA-PASA
        if t == 0:
            falta_pasa = None
        else:
            if 1 <= t <= 18:
                falta_pasa = "falta"
            elif 19 <= t <= 36:
                falta_pasa = "pasa"

        # paridad
        if t == 0:
            paridad = None
        else:
            if t % 2 == 0:
                paridad = "par"
            elif t % 2 != 0:
                paridad = "impar"
        
        # color
        if t == 0:
            color = None
        else:
            if t in rojos:
                color = "rojo"
            elif t in negros:
                color = "negro"

        # docena
        if t == 0:
            docena = None
        else:
            if t in docena_1:
                docena = "primera"
            elif t in docena_2:
                docena = "segunda"
            elif t in docena_3:
                docena = "tercera"

        # columna
        if t == 0:
            columna = None
        else:
            if t in columna_1:
                columna = "primera"
            elif t in columna_2:
                columna = "segunda"
            elif t in columna_3:
                columna= "tercera"

        # seisena
        if t == 0:
            seisena = None
        else:
            if t in columna_1:
                tt = t
            elif t in columna_2:
                idx = columna_2.index(t)
                tt = columna_1[idx]
            else:
                idx = columna_3.index(t)
                tt = columna_1[idx]
            
            if tt == 1:
                seisena = [1,2,3,4,5,6]
            elif tt == 34:
                seisena = [31,32,33,34,35,36]
            else:
                seisena1 = []
                seisena2 = []
                for i in range(tt-3,tt+3):
                    seisena1.append(i)
                for j in range(tt,tt+6):
                    seisena2.append(j)
                seisena = [seisena1] + [seisena2]

        # CUADRO
        if t == 0:
            cuadros = None
        else:
            cuadros = []
            if t == 0:
                cuadros = []
            elif t in columna_1:
                idx = columna_1.index(t)
                cuadros = gen_cuadro(idx,"columna_1")
            elif t in columna_3:
                idx = columna_3.index(t)
                cuadros = gen_cuadro(idx,"columna_3")
            else:
                idx = columna_2.index(t)
                cuadro1 = gen_cuadro(idx,"columna_1")
                cuadro2 = gen_cuadro(idx,"columna_3")
                cuadros = cuadro1 + cuadro2
        
        # transversal
        if t == 0:
            transversal = None
        else:
            if t in columna_1:
                idx = columna_1.index(t)
                transversal = [columna_1[idx],columna_2[idx],columna_3[idx]]
            elif t in columna_2:
                idx = columna_2.index(t)
                transversal = [columna_1[idx],columna_2[idx],columna_3[idx]]
            elif t in columna_3:
                idx = columna_3.index(t)
                transversal = [columna_1[idx],columna_2[idx],columna_3[idx]]
        
        # CABALLO
        if t == 0:
            caballos = None
        elif t in columna_1:
            idx = columna_1.index(t)
            caballos = gen_caballo(idx,"columna_1")
        elif t in columna_2:
            idx = columna_2.index(t)
            caballos = gen_caballo(idx,"columna_2")
        elif t in columna_3:
            idx = columna_3.index(t)
            caballos = gen_caballo(idx,"columna_3")

        return t, caballos, transversal, cuadros, seisena, columna, docena, color, paridad, falta_pasa
    
    def inicial(self):
        """Registra la banca incial del jugador"""
        while True:
            try:
                inicial = int(input("Indica tu banca inicial (en euros): "))
                print("Has registrado una banca inicial de " + str(inicial) + " euros.")
                e = str(input("Presiona S si es correcto y N en caso contrario: "))
                if e == "S" or e == "s":
                    print("De acuerdo.")
                    break       
                elif e == "N" or e == "n":
                    continue
                else:
                    print("Presiona solo S si es correcto y N en caso contrario.")
            except ValueError:
                print ("Error. Introduzca un numero entero. Comienza de nuevo.")

        return inicial
    
    def posibilidades_ganadoras(self):
        """Devuelve una lista con todas las posibilidades ganadoras"""
        t, caballos, transversal, cuadros, seisena, columna, docena, color, paridad, falta_pasa = self.tirada()
        return [[t], caballos, transversal, cuadros, seisena, columna, docena, color, paridad, falta_pasa]
       
    def decir_posibilidades(self):
        l = self.posibilidades_ganadoras()
        """Imprime todas las combinaciones ganadoras"""
        print("El numero que ha salido es el " + str(l[0]) + ". \nLas siguientes combinaciones son ganadoras: ")
        print("pleno: ", l[0],"\ncaballos: ", l[1], "\ntransversal: ", l[2], "\ncuadros: ", l[3], "\nseisena: ", 
            l[4], "\ncolumna: ", l[5], "\ndocena: ", l[6], "\ncolor: ", l[7], "\nparidad: ", l[8], "\nfalta_pasa: ", l[9])

    def registrar_apuesta(self):
        """Registra en un diccionario la apuesta y en otro la cantidad apostada"""

        apuesta = {"pleno":[],"caballos":[],"transversal":[],"cuadros":[],"seisena":[],"columna":[],"docena":[],"color":[],"paridad":[],"falta_pasa":[]}
        cantidad_a = {"pleno_a":[],"caballos_a":[],"transversal_a":[],"cuadros_a":[],"seisena_a":[],"columna_a":[],"docena_a":[],"color_a":[],"paridad_a":[],"falta_pasa_a":[]}

        print("Registre la apuesta")

        for key, value in apuesta.items():
            p = input("Quiere apostar " + key + "? (S/N): ")
            if p == "s":
                while True:
                    if key == "pleno":
                        #APUESTA PARA EL pleno, UNICA APUESTA QUE ES UN ENTERO
                        ap = int(input("Introduzca su apuesta: "))
                        value.append(ap)
                        a_ap = int(input("Introduzca el valor de su apuesta: "))
                        cantidad_a["pleno_a"].append(a_ap)

                        v = input("Quiere realizar otra apuesta? (S/N): ").lower()
                        if v == "s":
                            continue
                        else:
                            break

                    elif key == "caballos" or key == "transversal" or key == "cuadros" or key == "seisena":
                        #APUESTAS QUE SE REGISTRAN COMO LISTAS
                        ap = input("Introduzca su apuesta: ")
                        ap1=list(ap.split())
                        ap2=sorted(list(map(int,ap1)))
                        value.append(ap2)
                        a_ap = int(input("Introduzca el valor de su apuesta: "))
                        cantidad_a[key+"_a"].append(a_ap)

                        v = input("Quiere realizar otra apuesta? (S/N): ").lower()
                        if v == "s":
                            continue
                        else:
                            break

                    else:
                        #APUESTAS QUE SE REGISTRAN COMO STRINGS
                        ap = input("Introduzca su apuesta: ").lower()
                        value.append(ap)
                        a_ap = int(input("Introduzca el valor de su apuesta: "))
                        cantidad_a[key+"_a"].append(a_ap)

                        v = input("Quiere realizar otra apuesta? (S/N): ").lower()
                        if v == "s":
                            continue
                        else:
                            break
            else:
                pass
        return apuesta, cantidad_a
