#Control de temperartura
temp = 25
while temp > 0:
        temp  = float(input("ingrese temperatura: "))
        if temp >= 28:
            print("Encender aire acondicionado")
        elif temp  < 17:
            print("Encender calefaccion")
        else:("Temperatura agradable")
 