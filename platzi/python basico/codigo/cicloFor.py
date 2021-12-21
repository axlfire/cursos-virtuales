#-------main
def run():
    CicloForZeroTo()
    print(" ")
    CicloForXTo()
    print(" ")
    CicloFor2x2To()
#-------funciones
def CicloForZeroTo():
    print("numeros del 0 hasta el 100")
    for i in range(101):
        print(i)


def CicloForXTo():
    print("numeros desde X hasta 100")
    x= int(input("cual es el valor inicial? "))
    for i in range(x,101):
        print(i)


def CicloFor2x2To():
    print("numeros saltando de 2 en 2")
    for i in range(1,101,2):
        print(str(i-1)+"        "+str(i))
        if(i==99):
            print(100)
#---------config
if __name__ == '__main__':
    run()
