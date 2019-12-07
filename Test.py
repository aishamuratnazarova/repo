import unittest
import hello

class Test_TestOperations(unittest.TestCase):
    def test_add(self):
        self.assertTrue(hello.Calculator.Add(self))
    def test_devide(self):
        self.assertTrue(hello.Calculator.Divide(self))
    def test_modulo(self):
        self.assertEqual(hello.Calculator.Modulo(self))

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        