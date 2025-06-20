import unittest
from triangle import is_triangle

class TestTriangle(unittest.TestCase):

    def test_valid_triangles(self):
        """Test valid triangles"""
        self.assertTrue(is_triangle(3, 4, 5))
        self.assertTrue(is_triangle(5, 12, 13))
        self.assertTrue(is_triangle(10, 10, 10))  # Equilateral
        self.assertTrue(is_triangle(7, 8, 9))     # Scalene
        self.assertTrue(is_triangle(5, 5, 8))     # Isosceles

    def test_invalid_triangles(self):
        """Test invalid triangles"""
        self.assertFalse(is_triangle(1, 2, 3))    # 1+2 equals 3
        self.assertFalse(is_triangle(5, 10, 25)) # 5+10 < 25
        self.assertFalse(is_triangle(1, 1, 2))    # 1+1 equals 2

    def test_zero_or_negative(self):
        """Test with zero or negative values"""
        self.assertFalse(is_triangle(0, 0, 0))
        self.assertFalse(is_triangle(-1, 2, 3))
        self.assertFalse(is_triangle(1, -2, 3))
        self.assertFalse(is_triangle(1, 2, -3))
        self.assertFalse(is_triangle(0, 1, 1))

    def test_non_numbers(self):
        """Test with non-numeric values"""
        self.assertFalse(is_triangle("a", "b", "c"))
        self.assertFalse(is_triangle(1, 2, "3"))
        self.assertFalse(is_triangle(None, None, None))
        self.assertFalse(is_triangle([], [], []))

if __name__ == '__main__':
    unittest.main()