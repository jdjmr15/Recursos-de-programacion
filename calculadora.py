def main():
    print("Bienvenidos a mi primera calculadora en Python, espero que les guste.")
    print("")
    operacion = input("¿Qué operación deseas realizar? (+, -. *. /): ")
    print("")
    numero1 = float(input("Ingrese el primer valor : "))
    numero2 = float(input("Ingrese el segundo valor : "))

    print("")
    if operacion == "+":
        print("Resultado de la suma", numero1 + numero2)
    elif operacion == "-":
        
        print("Resultado de la resta", numero1 - numero2)
    elif operacion == "*":
        
        print("Resultado de la multiplicación", numero1 * numero2)
    elif operacion == "/":
        
        print("Resultado de la divisón", numero1 / numero2)
    else:
        print("Operación no válida")

    print("Hasta luego")
    print("")


if __name__ == '__main__':
    main()
