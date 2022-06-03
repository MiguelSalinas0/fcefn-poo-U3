import unittest

class TestPalabra(unittest.TestCase):
    
    def test_esPalindromo(self):
        self.assertTrue('menem')
    
    def test_esPalindromo1(self):
        self.assertTrue('neuquen')
    
    def test_esPalindromo2(self):
        self.assertFalse('alan')
    
    def test_esPalindromo3(self):
        self.assertFalse('gol')
    
    def test_esPalindromo4(self):
        self.assertTrue('otto')
    

if __name__=='__main__':
    unittest.main()
