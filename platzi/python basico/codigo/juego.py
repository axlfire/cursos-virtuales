from random import seed
from random import randint
import time
#------run()/main---
def run():
  adivino=True
  #crear la seed para la funcion random usando el reloj de el computador
  seedValue=int(time.time())
  seed(seedValue)
  value = randint(0,101)
  #ejecutar el juego
  while adivino:
     adivino=adivinar(value)
  print("adivinaste!!")
#------functions----
def adivinar(value):

    respuesta=int(input("ingresa cual numero crees es correcto entre 0 y 100: "))
    if(respuesta<value):
        print("el numero es mayor")
        return True
    elif(respuesta>value):
        print("el numero es menor")
        return True
    else:
        return False
#------config-------
if __name__ == '__main__':
    run()
