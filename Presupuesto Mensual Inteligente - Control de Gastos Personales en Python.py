# ===================================================================
# DESCRIPCIÓN GENERAL
# Este programa ayuda a cualquier persona a organizar su dinero mensual:
# - Pregunta salario y gastos reales
# - Calcula cuánto gasta y cuánto le queda para ahorrar
# - Da recomendaciones personalizadas según sus hábitos
# - Muy útil para aprender educación financiera
# ===================================================================

"""
 ------------------------------
 Función para pedir números enteros al usuario con validación
 ------------------------------
"""
def pedir_numero(mensaje: str) -> int: 
    """
    Pide un número entero al usuario.
    Si escribe letras o símbolos, muestra error y vuelve a preguntar.
    Ejemplo: "Ingrese su salario mensual: "
    """
    while True:  # Se repite hasta que el usuario escriba un número válido
        try:
            return int(input(mensaje))  # Convierte lo escrito a número
        except ValueError:
            print("Error: ingrese un número válido, 5.0/5.0 válido. ¡Solo números enteros!")  # Mensaje claro de error

"""
 ------------------------------
 Función para validar el tipo de vivienda
 ------------------------------
"""
def pedir_tipo_vivienda() -> str:
    """
    Pregunta si la vivienda es 'propia' o 'arrendada'.
    Solo acepta esas dos palabras (en minúscula).
    Si escribe otra cosa, insiste hasta que lo haga bien.
    """
    while True:
        tipo = input("Escriba si tiene vivienda 'propia' o 'arrendada': ").lower()  # .lower() acepta mayúsculas
        if tipo in ["propia", "arrendada"]:
            return tipo  # Devuelve la opción válida
        print("Opción inválida. Solo escriba: 'propia' o 'arrendada'.")

"""
 ------------------------------
 Función que calcula cuánto gastas y cuánto ahorras
 ------------------------------
"""
def calcular_presupuesto(salario: int, vivienda: str, arriendo: int, facturas: int, otros: int, ahorro_deseado: int):
    """
    Calcula:
    - egresos = todo lo que gastas (arriendo + servicios + comida/ocio)
    - ahorros = salario - egresos (lo que realmente te sobra)
    Devuelve ambos valores como una tupla.
    """
    egresos = arriendo + facturas + otros  # Suma todos los gastos fijos y variables
    ahorros = salario - egresos             # Lo que te queda después de pagar todo
    return egresos, ahorros                 # Devuelve dos valores

"""
 ------------------------------
 Función que muestra resultados bonitos y da consejos
 ------------------------------
"""
def mostrar_resultados(egresos: int, ahorros: int, ahorro_deseado: int, otros: int, facturas: int):
    """
    Muestra el resumen financiero y da consejos inteligentes:
    - Si gastas más en cine/comida que en servicios → te regaña un poquito
    - Si no llegas al ahorro que querías → te motiva a reducir gastos hormiga
    - Si lo lograste → ¡te felicita!
    """
    print(f"\nSus egresos mensuales son: ${egresos:,}")
    print(f"Sus ahorros mensuales son: ${ahorros:,}")

    # Alerta si gastas demasiado en ocio/comida
    if otros >= facturas:
        print("sus gastos en otros servicios son muy elevados, deberia intentar ir menos al cine")

    # Compara tu meta de ahorro con la realidad
    if ahorro_deseado > ahorros:
        print("Debe tomar medidas para llegar al ahorro deseado, puede comenzar quitando los gastos hormiga.")
    else:
        print("bien hecho, tus deseos se han hecho realidad")


"""
 ------------------------------
 Función principal - Aquí empieza todo
 ------------------------------
"""
def main():
    """
    Función principal que coordina todo el programa:
    1. Saluda y pide todos los datos
    2. Calcula el presupuesto
    3. Muestra resultados con consejos
    """
    print("=== PLANIFICADOR FINANCIERO PERSONAL ===")
    print("¡Vamos a ver cuánto dinero te queda realmente cada mes!\n")

    # === ENTRADA DE DATOS ===
    salario = pedir_numero("Ingrese su salario mensual: $")
    vivienda = pedir_tipo_vivienda()
    
    # Si vive arrendado, pregunta cuánto paga. Si es propia → arriendo = 0
    arriendo = pedir_numero("Ingrese el gasto de arriendo: $") if vivienda == "arrendada" else 0
    
    facturas = pedir_numero("Ingrese el promedio de gastos en servicios (luz, agua, internet): $")
    otros = pedir_numero("Ingrese el promedio en comida fuera, cine, salidas, etc: $")
    ahorro_deseado = pedir_numero("¿Cuánto dinero deseas ahorrar al mes?: $")

    # === CÁLCULO ===
    egresos, ahorros = calcular_presupuesto(salario, vivienda, arriendo, facturas, otros, ahorro_deseado)
    
    # === RESULTADOS ===
    mostrar_resultados(egresos, ahorros, ahorro_deseado, otros, facturas)

    print("\n¡Gracias por usar el planificador! Recuerda: el primer paso para ser rico es saber a dónde va tu dinero")


"""
 ------------------------------
 Ejecuta el programa solo si se corre directamente
 ------------------------------
"""
if __name__ == "__main__":
    main()