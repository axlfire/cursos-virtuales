#esta funcion es la que contiene el programa, digamos que es el main
def run():
    palabra=input("que palabra o frase crees que es un palindromo?: ")
    palabraInv=palabra[::-1]
    comparar(palabra,palabraInv)
#funciones----------------------------------------------
def comparar(str1,str2):
    #esto elimina los espacios de la frase, y pone todas las letras en minusculas
    str3=str1.replace(' ','')
    str4=str2.replace(' ','')
    str4=str4.lower()
    str3=str3.lower()

    if(str3==str4):
        print("si \""+str1+"\" y \""+str2+"\" son iguales")
    else:
        print("no,\""+str1+"\" y \""+str2+"\" no son iguales")



#----------------------------------------------------------------

if __name__ == '__main__':
    run()
