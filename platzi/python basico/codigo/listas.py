#---imports/const---


#------run()/main---
def run():
  listaNumeros=[0,10,23,3,4,5]
  ListaPalabras=["simon","arroz","lechuga"]
  listaVarios=["arbol","aguacate",1,True,'q']
  listaVacia=[]
  print("leer lista de numeros")
  print(listaNumeros)
  print(" ")
  print("leer lista de palabras")
  print(ListaPalabras)
  print(" ")
  print("leer lista de varios tipos")
  print(listaVarios)
  print(" ")
  print("añadir elementos a una lista")
  addElem(ListaPalabras,"tomate")
  print(ListaPalabras)
  print(" ")
  print("eliminar el ultimo elemento de una lista")
  delElem(ListaPalabras)
  print(ListaPalabras)
  print(" ")
  print("imprimir con un for cada elemento de la lista")
  printElem(listaVarios)
  print(" ")
  print("ordenar elementos de una lista")
  ordenar(listaNumeros)
  print(listaNumeros)
  print(" ")
  print("crear una lista en un rango de numeros")
  print("estado de lista actual:"+str(listaVacia))
  listaVacia=(list(range(0,42,3)))
  print("lista despues de poblarla: "+str(listaVacia))
  print(" ")
  print("eliminar numeros pares de la lista anterior: ")
  DelPairElem(listaVacia)
  print(listaVacia)
  print(" ")
  print("invertir la lista y guardarlos")
  listaInvertida=listaVacia[::-1]
  print(listaInvertida)
  print(" ")
  print("imprimir una lista desde x hasta Y")
  print(listaVarios[1:4:1])
  #------functions----
def addElem(lista,elemento):
    lista.append(elemento)


def delElem(lista):
    lista.pop(int(len(lista))-1)


def printElem(lista):
    for elemento in lista:
        print("elemento: "+str(elemento))


def DelPairElem(lista):
    try:
        lista.remove(range(0,len(lista)-1,2) )
    except Exception as e:
        pass


def ordenar(lista):
    lista.sort()



#------config-------
if __name__ == '__main__':
    run()
