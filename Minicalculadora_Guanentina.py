import math as mt


print("----------------------------------")
print("1) suma")
print("2) resta")
print("3) multiplicación")
print("4) división")
print("5) potenciación")
print("6) logaritmos")
print("-----------------------------------")

opc = int(input("digite el número correspondiente a la operacion: "))
    
x = int(input("digite el primer número de la operación: "))
y = int(input("digite el segundo número de la operación: "))


if opc == 1:
    print(f"el resultado de la suma es {(x)+(y)}")

elif opc == 2:
    print(f"el resultado de la resta es {(x)-(y)}")

elif opc == 3:
    print(f"el resultado de la multiplicación es {(x)*(y)}")

elif opc == 4:
    if y <= 0:
        print("Error.")
    else:
        print(f"el resultado de la división es {(x)/(y)}")

elif opc == 5:
    print(f"el resultado de la potenciación es {(x)**(y)}")

elif opc == 6:
    logaritmo = mt.log(y,x)
    print(f"el resultado del logaritmo es {logaritmo}")

else:
    print("no valido")