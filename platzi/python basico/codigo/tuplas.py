#---imports/const---


#------run()/main---
def run():
  tupla=("efe","aguacate",12,False,True,"efe",12,13,1,0,2)
  print("tupla: "+str(tupla))
  print("")
  #no se pueden añadir elementos a las tuplas o eliminar
  print("contar que tanto se repite algo usando \'.count()\':")
  print(tupla.count('efe'))
  print("")
  print("tupla de un solo elemento")
  tupla1=("elemento")
  print(tupla1)
  print(" ")
  #empaquetar datos en una tupla:
  tuplaEmpac="suarez",22,8,99
  print("print de los datos de una tupla(desempaquetado):")
  nombre,edad,mes,año=tuplaEmpac
  print("nombre: "+nombre)
  print("edad: "+str(edad))
  print("mes: "+str(mes))
  print("año: "+str(año))
  print(" ")
  #empaquetado y desempaquetado usando funciones usando funciones
  pais,dinero,religion=funcionTupla()
  print("")
  print("imprimir datos de una tupla usando una funcion y desempaquetando: ")
  print("pais: "+pais)
  print("dinero: "+dinero)
  print("religion: "+religion)
#------functions----
def funcionTupla():
    pais=input("pais? ")
    dinero=input("cuanto dinero tienes en "+pais+"?: ")
    religion=input("que religion tiene "+pais+"?: ")
    return (pais,dinero,religion)
#------config-------
if __name__ == '__main__':
    run()
