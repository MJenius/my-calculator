"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""
import pytest
from src.calculator import add, divide, subtract,multiply,power,sqrt

class TestBasicOperations:
    """Test basic arithmetic operations"""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6

    def test_add_negative_numbers(self):
        """Test adding negative numbers"""
        assert add(-1,-2)==-3
        assert add(-5,-3)==-8

    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers"""
        assert subtract(-5,-3)==-2
        assert subtract(-10,-4)==-6

class TestMultiplyDivideWithValidation:
    """Test multiplication and division with input validation."""
    
    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(5, "3")
    
    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)

    def test_power_input_validation(self):
        """Test power rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            power("5", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            power(5, "3")
        
    def test_power_positive_numbers(self):
        """Test power with positive numbers"""
        assert power(2, 3) == 8

    def test_power_negative_numbers(self):
        """Test power with negative numbers"""
        assert power(-2, 3) == -8

    def test_power_zero(self):
        """Test power with zero"""
        assert power(0, 3) == 0
        assert power(5, 0) == 1

    def test_squareroot_positive_numbers(self):
        """Test square root with positive numbers"""
        assert sqrt(4) == 2
    
    def test_squareroot_negative_numbers(self):
        """Test square root with negative numbers"""
        assert sqrt(-4) == -2

    def test_squareroot_zero(self):
        """Test square root with zero"""
        assert sqrt(0) == 0


# TODO: Students will add TestMultiplyDivide class

class TestMultiplyDivide:
    """Test multiplication and division operations"""
    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers"""
        assert multiply(2, 3) == 6
        assert multiply(10, 5) == 50

    def multiply_by_zero(self):
        """Test multiplying by zero"""
        assert multiply(5, 0) == 0
        assert multiply(0, 10) == 0

    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers"""
        assert multiply(-2, -3) == 6
        assert multiply(-5, -3) == 15

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers"""
        assert divide(10, 2) == 5
        assert divide(20, 4) == 5
        
    def test_divide_negative_numbers(self):
        """Test dividing negative numbers"""
        assert divide(-10, 2) == -5
        assert divide(-20, 4) == -5
