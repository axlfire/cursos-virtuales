#------run()/main---
def run():
  print("usando continue: ")
  continuefunc()
  print("usando break: ")
  breakfunc()
  print("recorrer una cadena ")
  recorrerTxtHasta()
  print("break while ")
  breakwhile()
#------functions----
def continuefunc():
    for i in range(1001):
        if i%2!=0:
            #continue hace que no se ejecute el resto de el codigo
            #pero se quede dentro de el ciclo
            continue
        print(str(i))


def breakfunc():
    for i in range(1001):
        print(str(i))
        if i>=550:
            break


def recorrerTxtHasta():
    texto=input("ingresa un texto: ")
    for letra in texto:
        if letra=='o':
            print("aqui habia una o")
            break
        print(letra)


def breakwhile():
    i=0
    while i<=30:
        print(str(i))
        if i>=25:
            break
        i=i+1
#------config-------
if __name__ == '__main__':
    run()
