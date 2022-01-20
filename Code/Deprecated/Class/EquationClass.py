from scipy.integrate import quad
import sympy as smp

class NumericSolve:
    """A class of Equation, built in function of solving integrations using numeric values,
        ## __equation__: 
            # a FUNCTION of equation, for example:
            def equation(x, a, b):
               return a*x**2 + b
        ## __args__: 
            # A dictionary store argument of equations defined
            args = {
                "a":2,
                "b":3
                }
        """
    def __init__(self, equation):
        self.equation = equation
    
    def solve(self, boundary, args):
        """Solve the function by taking Integration, return value"""
        result = quad(self.equation, boundary[0], boundary[1], args=args)
        print("Solution:", result[0])
        print("Error:", result[1])
        return result[0]


class SymbolicSolve:
    """A class of Equation, built in function of solving integrations in symbolic form,
        ## __equation__: 
            # a FUNCTION of equation, for example:
            def equation(x, a, b):
               return a*x**2 + b
        ## __args__: 
            # A dictionary store argument of equations defined
            args = {
                "a":2,
                "b":3
                }
        """
    def __init__(self, equation):
        self.equation = equation
    
    def solve(self, boundary, args):
        """Solve the function by taking Integration, return value"""
        result = quad(self.equation, boundary[0], boundary[1], args=args)
        print("Solution:", result[0])
        print("Error:", result[1])
        return result[0]