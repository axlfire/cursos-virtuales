cadena=input("ingrese una palabra ")

print("upper= "+cadena.upper()+".")
print("capitalize= "+cadena.capitalize()+".")
control=cadena.capitalize();
print("#este le quita espacios extras[ strip= "+control.strip()+".")
print("lower= "+cadena.lower()+".")
print("replace(e,i)= "+cadena.replace('e','i')+".")
print("index cadena[x] "+cadena[0]+(".")+cadena[1]+("."))
longitudCadena=str(len(cadena))
print(("len: ")+longitudCadena+("."))
print(("join: "+cadena.join("aguacate")))
