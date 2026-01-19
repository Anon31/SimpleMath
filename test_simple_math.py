"""
Module de tests unitaires pour la classe SimpleMath.
"""
import unittest
from simple_math import SimpleMath

class TestSimpleMath(unittest.TestCase):
    """
    Classe de tests unitaires héritant de unittest.TestCase.
    """

    def test_addition(self):
        """Test de la méthode addition."""
        self.assertEqual(SimpleMath.addition(2, 3), 5)
        self.assertEqual(SimpleMath.addition(-1, 1), 0)

    def test_soustraction(self):
        """Test de la méthode soustraction."""
        self.assertEqual(SimpleMath.soustraction(5, 3), 2)
        self.assertEqual(SimpleMath.soustraction(0, 5), -5)

if __name__ == '__main__':
    unittest.main()