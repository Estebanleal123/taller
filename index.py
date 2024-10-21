class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

def deberiaDefinirComoPrioritariaAUnaPersonaDeMasDe60Años(persona):
    return persona.edad > 60

# Ejemplo de uso
persona1 = Persona("Juan", 65)
print(deberiaDefinirComoPrioritariaAUnaPersonaDeMasDe60Años(persona1)) 