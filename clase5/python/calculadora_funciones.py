


num1 = float(input("Ingrese el primer número: "))
operador = input("Ingrese el operador (+, -, *, /): ")
num2 = float(input("Ingrese el segundo número: "))

match operador:
    case '+':
        resultado = sumar(num1,num2)
    case '-':
        resultado = restar(num1,num2)
    case '*':
        resultado = multiplicar(num1,num2)
    case '/':
        if num2 != 0:
            resultado = dividir(num1,num2)
        else:
            resultado = num1 / 1
    case _:
        operador = 'error'
        
if resultado != 'error':
    print(f"Resultado del operador '{operador}' es: {resultado}")
else:
    print(f"Error al elegir el operador. Los operadores válidos son: +,-,*, y /")