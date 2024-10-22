def definir_prioridad(persona):
    """Devuelve si la persona es prioritaria según su edad."""
    if persona['edad'] > 60:
        return f"{persona['nombre']} es una persona prioritaria."
    else:
        return f"{persona['nombre']} no es una persona prioritaria."

def main():
    # Ejemplo de personas
    personas = [
        {"nombre": "Juan", "edad": 65},
        {"nombre": "Maria", "edad": 30},
        {"nombre": "Luis", "edad": 70}
    ]

    for persona in personas:
        resultado = definir_prioridad(persona)
        print(resultado)

if __name__ == "__main__":
    main()