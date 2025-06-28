import unittest
from sitio import contar_vocales

class TestContarVocales(unittest.TestCase):
    def test_contar_vocales(self):
        self.assertEqual(contar_vocales("hola"), 2)
        self.assertEqual(contar_vocales("HELLO"), 2)  # Assuming case insensitivity
        self.assertEqual(contar_vocales("xyz"), 0)
        self.assertEqual(contar_vocales("aeiou"), 5)
        self.assertEqual(contar_vocales(""), 0)

if __name__ == '__main__':
    unittest.main()

