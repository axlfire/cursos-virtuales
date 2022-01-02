#---imports/const---


#------run()/main---
def run():
#un diccionario es un array de datos los cuales son referenciados
#por medio de  llaves
  diccionario={
    'llave1':1,
    'llave2':2,
    'llave3':3,
    'llave4':4
  }

  print("diccionario: "+str(diccionario))
  print("")
  #A los datos se accede por medio de las llaves asi:
  print("")
  print("llave 1: "+str(diccionario['llave1']))
  #----------------------------------------------------
  print("")
  print("obtener todas las keys usando for: ")
  print(recorrerDiccionarioLlaves(diccionario))
  #----------------------------------------------------
  print("")
  print("obtener todos los valores usando for: ")
  print(recorrerDiccionarioValues(diccionario))
  #----------------------------------------------------
  print("")
  print("recorrer diccionario obteniendo keys y valores")
  print(recorrerDiccionario(diccionario))

  
#------functions----
def recorrerDiccionarioLlaves(diccionario):
    for llave in diccionario.keys():
        print(llave)


def recorrerDiccionarioValues(diccionario):
    for value in diccionario.values():
        print(value)

def recorrerDiccionario(diccionario):
    #.items() devuelve resultados como lo haria una tupla
    #por eso es que se lee y se asigna valores de esta manera
    for key,value in diccionario.items():
        print(key+" es la llave para el valor: "+str(value))
#------config-------
if __name__ == '__main__':
    run()
