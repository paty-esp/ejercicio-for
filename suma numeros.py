cant=int(input("ingresa numeros para sumar:"))
suma=0
for i in range(cant):
    numero=float(input(f"ingresa el otro numero para sumar{i+1}: "))
    suma+=numero
    print(f"suma total:{suma}")
