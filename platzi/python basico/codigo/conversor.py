valor_dolar=3875
valor_peso_argentino=1000
valor_bolivares=0.001

#funciones--------------------------------------------------------------------

def calcular_valor(valor_COP,valor_conversor):
    valor=str(valor_COP/valor_conversor)
    return valor
#"main"--------------------------------------------------------------------------------
pais=str(input("a que pais deseas convertir la moneda(argentina)(venezuela)(EEUU) "))
pesos=float(input("¿texto que pide valor monetario COP?"))

if pais=="argentina":
    valor_conv=calcular_valor(pesos,valor_peso_argentino)
    print("tiene "+ valor_conv +" peso argentino")

elif pais=="venezuela":
    valor_conv=calcular_valor(pesos,valor_bolivares)
    print("tiene "+ valor_conv+" memedolares bolivarianos")

else:
    valor_conv=calcular_valor(pesos,valor_dolar)
    print("tiene "+ valor_conv+" dolares")
