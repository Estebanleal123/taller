import unittest

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

def es_prioritario(persona):
    """Determina si una persona es prioritaria (mayor de 60 años)."""
    return persona.edad > 60

class TestPrioridad(unittest.TestCase):
    def test_deberia_definir_como_prioritaria_a_una_persona_de_mas_de_60(self):
        persona_mayor = Persona("Juan", 65)
        persona_joven = Persona("Ana", 30)

        # Verificamos que la persona mayor sea considerada prioritaria
        self.assertTrue(es_prioritario(persona_mayor), "La persona mayor debería ser prioritaria.")
        
        # Verificamos que la persona joven no sea considerada prioritaria
        self.assertFalse(es_prioritario(persona_joven), "La persona joven no debería ser prioritaria.")

if __name__ == '__main__':
    unittest.main()