def par_impar():
    num = int(input("Ingrese un numero: "))
    if num % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")


def factorial():
    num = int(input("Ingrese numero: "))
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    print("El factorial es:", resultado)


def tabla():
    num = int(input("Ingrese numero: "))
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)


def menu():
    while True:
        print("\nUTILIDADES")
        print("1. PAR O IMPAR")
        print("2. FACTORIAL")
        print("3. TABLA DE MULTIPLICAR")
        print("4. SALIR")

        opcion = int(input("Seleccione opcion: "))

        if opcion == 1:
            par_impar()
        elif opcion == 2:
            factorial()
        elif opcion == 3:
            tabla()
        elif opcion == 4:
            print("Saliendo...")
            break
        else:
            print("Opción no válida")

menu()



