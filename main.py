from funciones import *

print("BIENVENIDO AL JUEGO DE LA RULETA!")
rul = Ruleta()

banca_inicial = rul.inicial()
while True:
    apuesta, cantidad_a = rul.registrar_apuesta()
    print("GIRANDO LA RULETA! GIRANDO LA RULETA!")
    pos_ganadoras = rul.posibilidades_ganadoras()
    ganancias, perdidas = comprobar_apuesta(apuesta, cantidad_a, pos_ganadoras)
    ganado = sum(ganancias)
    perdido = sum(perdidas)
    print("HA SALIDO EL NUMERO " + str(pos_ganadoras[0]))
    print("ENHORABUENA! HA GANADO " + str(ganado) + " PERO HA PERDIDO " + str(perdido))
    banca_inicial = banca_inicial + ganado - perdido
    if banca_inicial <= 0:
        print("PERDIO SU DINERO. SU BANCA ES DE " + str(banca_inicial))
        print("NO PUEDE SEGUIR JUGANDO")
        break
    print("SU DINERO TOTAL ES DE ",banca_inicial," EUROS!")
    rul = Ruleta()
    v = input("DESEA SEGUIR JUGANDO? (S/N): ").lower()
    if v == "n":
        print("QUE PASE UN BUEN DIA!")
        break
