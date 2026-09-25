productos = ["Arroz", "Aceite", "Fideo", "Azucar"]

with open("archivo.txt", "w") as archivo: 
    for p in productos:
        archivo.write(f"{p} \n")

print("lista de productos desde el archivo:")        
with open("archivo.txt", "r" , encoding="utf-8") as archivo:
    lineas = archivo.readlines()
    for p in lineas:
        print(p.strip())
        

        