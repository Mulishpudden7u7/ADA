class Pila:
    def __init__(self):
        self.items = []

    def vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()


def evaluar_expresion_posfija(expresion):
    pila = Pila()
    operandos = expresion.split()

    for token in operandos:
        if token.isdigit():
            pila.apilar(int(token))
        else:
            operando2 = pila.desapilar()
            operando1 = pila.desapilar()
            resultado = realizar_operacion(token, operando1, operando2)
            pila.apilar(resultado)

    return pila.desapilar()


def evaluar_expresion_prefija(expresion):
    pila = Pila()
    operandos = expresion.split()[::-1]  

    for token in operandos:
        if token.isdigit():
            pila.apilar(int(token))
        else:
            if len(pila.items) < 2:
                raise ValueError("No hay suficientes operandos para la operación.")
            
            operando1 = pila.desapilar()
            operando2 = pila.desapilar()
            resultado = realizar_operacion(token, operando1, operando2)
            pila.apilar(resultado)

    return pila.desapilar()


def realizar_operacion(operador, op1, op2):
    if operador == '+':
        return op1 + op2
    elif operador == '-':
        return op1 - op2
    elif operador == '*':
        return op1 * op2
    elif operador == '/':
        return op1 / op2
    else:
        raise ValueError("Operador no válido")


def main():
    tipo_evaluacion = input("¿Cómo desea evaluar la expresión? (posfija/prefija): ").lower()

    if tipo_evaluacion == 'posfija':
        expresion_aritmetica = "3 4 + 2 *"
        resultado = evaluar_expresion_posfija(expresion_aritmetica)
        print("El resultado de la expresión en notación posfija es:", resultado)
    elif tipo_evaluacion == 'prefija':
        expresion_aritmetica = "* + 3 4 2"
        resultado = evaluar_expresion_prefija(expresion_aritmetica)
        print("El resultado de la expresión en notación prefija es:", resultado)
    else:
        print("Opción no válida. Por favor, seleccione 'posfija' o 'prefija'.")


if __name__ == "__main__":
    main()
