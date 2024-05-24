import funciones_calculadora as fc

def mostrar_menu(a, b):
    """Muestra el menú principal con los valores actuales de A y B."""
    print(f"\nCalculadora")
    print(f"1. Ingresar 1er operando (A={a})")
    print(f"2. Ingresar 2do operando (B={b})")
    print(f"3. Calcular todas las operaciones")
    print(f"4. Informar resultados")
    print(f"5. Salir")

def ingresar_operando(mensaje):
    """Solicita al usuario ingresar un operando.
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario.
    
    Returns:
        float: El operando ingresado por el usuario.
    """
    return float(input(mensaje))

def main():
    a = 0
    b = 0
    resultados = {}

    while True:
        mostrar_menu(a, b)
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            a = ingresar_operando("Ingrese el 1er operando: ")
        elif opcion == '2':
            b = ingresar_operando("Ingrese el 2do operando: ")
        elif opcion == '3':
            resultados['suma'] = fc.sumar(a, b)
            resultados['resta'] = fc.restar(a, b)
            resultados['division'] = fc.dividir(a, b)
            resultados['multiplicacion'] = fc.multiplicar(a, b)
            resultados['factorial_a'] = fc.factorial(int(a))
            resultados['factorial_b'] = fc.factorial(int(b))
        elif opcion == '4':
            if resultados:
                print(f"El resultado de A+B es: {resultados['suma']}")
                print(f"El resultado de A-B es: {resultados['resta']}")
                print(f"El resultado de A/B es: {resultados['division']}")
                print(f"El resultado de A*B es: {resultados['multiplicacion']}")
                print(f"El factorial de A es: {resultados['factorial_a']} y el factorial de B es: {resultados['factorial_b']}")
            else:
                print("Primero debe calcular las operaciones (opción 3).")
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

main()