from scipy.integrate import quad

class Equation:
    """A class of Equation, built in function of solving integrations,
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
    
    def solve_integration(self, boundary, args):
        """Solve the function by taking Integration"""
        return quad(self.equation, boundary[0], boundary[1], args=args)