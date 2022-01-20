from Class.EquationClass import *


### Symbolic Solve:

# Set Symbols
x = smp.symbols('x', real=True)
a, b = smp.symbols('a b', real=True, positive=True)
# Define Function f
F = smp.cos(b*x)* smp.exp(-a*x)

## Solve the function
sol_2 = smp.integrate(F, x).simplify()
print(sol_2)



### Numerical Solve

## Define Equation like this:
def integrand(x, a, b):
    return a*x**2 + b


### Create an Equation Class
CCC_model_numeric = NumericSolve(integrand)


### Solve Integration
#1. Numeric Solve
# Please put arguments in order of the function argument defined above
equation_args = (
    2, #a
    1  #b
   )   ## Take all arguments from above defined equations
integration_boundary = [0, 1]  # use +inf for infinity

sol = CCC_model_numeric.solve(integration_boundary, equation_args)
print(sol)

#2. Symbolic Solve

