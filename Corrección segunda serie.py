mail = input("Ingrese su mail: ") 
cantidad = 0  
x = 0  
while x < len(mail):  
    if mail[x] == "e" or mail[x] == "n":
        cantidad = cantidad + 1
    x = x + 1  
if cantidad == 1:
    print("Contiene solo un carácter 'e' o 'n' en el mail ingresado") 
else:
    print("Incorrecto") 