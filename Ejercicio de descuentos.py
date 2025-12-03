# Inicia el bucle infinito que solo se detiene con 'TERMINAR PROCESO'
while True:
    
    # Pedir Entrada (Como texto)
    entrada_texto = input("\nIngrese el monto de la compra: ").upper().strip()

    # VERIFICACIÓN DE SALIDA SECRETA
    if entrada_texto == "TERMINAR PROCESO":
        break # Sale del bucle

    # MANEJO DE ERRORES (TRY/EXCEPT)
    try:
        monto_de_compra = float(entrada_texto) 
        
    except ValueError:
        # Se ejecuta si el usuario ingresó algo que NO es 'TERMINAR PROCESO' y NO es un número.
        print("¡ERROR! Ingrese un valor numérico válido. Intente de nuevo.")
        continue # Vuelve al inicio del bucle

    # LÓGICA DE CÁLCULO (Se ejecuta solo si la entrada es un número válido)
    if monto_de_compra > 10000:
        descuento = 0.1 * monto_de_compra
    else:
        descuento = 0
            
    # SALIDA DE RESULTADOS
    total_a_pagar = monto_de_compra - descuento
    
    # Usamos round() para la limpieza visual de los decimales
    print("El monto de la compra es: ", round(monto_de_compra))
    print("El descuento es: ", round(descuento))
    print("El total a pagar es: ", round(total_a_pagar))

print("\n>>> Programa finalizado. ¡Gracias por usar nuestro servicio! <<<")