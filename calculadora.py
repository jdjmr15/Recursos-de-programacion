def main():
    operador = ""
    print("Bienvenidos a mi primera calculadora en Python, espero que les guste.")
    print("")
    operacion = input("¿Qué operación deseas realizar? (+, -. *. /): ")
    print("")
    num1 = float(input("Ingrese el primer valor : "))
    num2 = float(input("Ingrese el segundo valor : "))

    print("")

    match operacion:
        case '+':
            resultado = num1 + num2
        case '-':
            resultado = num1 - num2
        case '*':
            resultado = num1 * num2
        case '/':
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = num1 / 1
        case _:
            operador = 'error'

    if operador != 'error':
        print(f"Resultado del operador '{operacion}' es: {resultado}")
    else:
        print(f"Error al elegir el operador. Los operadores son +, -, *, y /")

    print("Hasta luego")
    print("")


if __name__ == '__main__':
    main()
