def pedir_texto_sin_numeros(prompt):
    while True:
        texto = input(prompt).strip()
        if not texto:
            print("Por favor ingresa texto (no vacío). Intenta de nuevo.")
            continue
        if any(ch.isdigit() for ch in texto):
            print("No se permiten números aquí. Ingresa sólo letras y espacios.")
            continue
        return texto

def pedir_edad(prompt):
    while True:
        s = input(prompt).strip()
        if not s:
            print("Por favor ingresa tu edad en números. Intenta de nuevo.")
            continue
        if not s.isdigit():
            print("La edad debe ingresarse con dígitos únicamente. Intenta de nuevo.")
            continue
        edad_val = int(s)
        if edad_val < 0 or edad_val > 120:
            print("Ingresa una edad válida (0-120). Intenta de nuevo.")
            continue
        return edad_val

# Interacción con el usuario (Entrada de datos) con validaciones
nombre = pedir_texto_sin_numeros("Ingresa tu nombre: ")
institucion = pedir_texto_sin_numeros("¿En qué institución estudias?: ")
edad = pedir_edad("¿Qué edad tienes?: ")

print("-" * 30)  # Línea divisoria para que se vea ordenado

# Mostrar el mensaje (Salida de datos)
print("Estudiante: " + nombre)
print("Sede: " + institucion)
print("Edad actual: " + str(edad))

# Lógica de decisión
if edad >= 18:
    print("Estado: Listo para el éxito en Marzo.")
else:
    print("Estado: Aún eres menor de edad para este proceso.")