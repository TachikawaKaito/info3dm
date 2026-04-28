import unittest
import dataset1

class TestStringMethods(unittest.TestCase):
    def test_x_0(self):
        y = dataset1.true_function(0)
        self.assertEqual(y, 0)

if __name__ == '__main__':
    unittest.main()