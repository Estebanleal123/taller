def definir_prioridad(persona):
    """Devuelve la prioridad de la persona según su edad."""
    if persona['edad'] > 60:
        return f"{persona['nombre']} es una persona prioritaria."
    elif persona['edad'] < 30:
        return f"{persona['nombre']} es una persona joven y no prioritaria."
    elif 30 <= persona['edad'] <= 60:
        return f"{persona['nombre']} es una persona adulta y no prioritaria."
    else:
        return f"{persona['nombre']} no tiene una categoría definida."

def main():
    # Ejemplo de personas
    personas = [
        {"nombre": "Juan", "edad": 65},
        {"nombre": "Maria", "edad": 30},
        {"nombre": "Luis", "edad": 70},
        {"nombre": "Ana", "edad": 25},
        {"nombre": "Carlos", "edad": 45}
    ]

    for persona in personas:
        resultado = definir_prioridad(persona)
        print(resultado)

if __name__ == "__main__":
    main()