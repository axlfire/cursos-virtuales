#---imports/const---
import random

#------run()/main---
def run():
    mayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    minus = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    esp = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']',
             ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    caracteres=[]
    long=int(input("que tan larga quiere la contraseña? "))
    espcar,numcar,minuscar,mayuscar=caracteresValidos()
    if minuscar:
        caracteres=caracteres+minus
    if mayuscar:
        caracteres=caracteres+mayus
    if espcar:
        caracteres=caracteres+esp
    if numcar:
        caracteres=caracteres+nums

    miContrasena=generarContrasena(caracteres,long)

    print(f"tu contraseña es: {miContrasena }")
#------functions----
def caracteresValidos():
    print("ingrese 'Y' en caso de respuesta afirmativa, de lo contrario se considera una negacion:")
    print("quiere caracteres especiales?")
    espcar=trueFalse()
    print("quiere numeros?")
    numcar=trueFalse()
    print("quiere minusculas?")
    minuscar=trueFalse()
    print("quiere mayusculas?")
    mayuscar=trueFalse()
    return(espcar,numcar,minuscar,mayuscar)




def generarContrasena(cadena,long):
    contrasena=[]
    for i in range(long):
        caracter=random.choice(cadena)
        contrasena.append(caracter)
    #convierte una lista en string
    return ("".join(contrasena))


def trueFalse():
    respuesta=input()
    if respuesta.lower()=="y":
        return True
    else:
        return False

#------config-------
if __name__ == '__main__':
    run()
