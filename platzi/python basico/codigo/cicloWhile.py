#---variables globales----------------
    #constantes se definen con mayusculas
LIMITE=1000

#-------------main-------------------
def run():
    contador=0
    potencia(contador)
#----------funciones-----------------
def potencia(cont):
    potencia2=0
    while potencia2<LIMITE :
        potencia2=2**cont
        print("2 elevado a "+str(cont)+" es igual a: "+str(potencia2))
        cont+=1

#---------config------------------------
if __name__ == '__main__':
    run()
