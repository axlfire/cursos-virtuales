#------run()/main---
def run():
    print("recorer nombre")
    recorrerNombre()
    print()
    recorrer2n2()
#------functions----
def pedirNombre():
    nombre=input("cual es tu nombre?: ")
    return nombre

def recorrerNombre():
    nombre=pedirNombre()
    for letra in nombre:
        print(letra)

# def recorrer2n2():
#     nombre=pedirNombre()
#     cadLong=len(nombre)
#     for letra in nombre[0,cadLong,2]:
#         print(letra)
#
#
def recorrer2n2 ():
    nombre=pedirNombre()
    for letra in range(0,len(nombre),2):
        print(nombre[int(letra)])


#------config-------
if __name__ == '__main__':
    run()
