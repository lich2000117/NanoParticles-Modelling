from Class.EquationClass import Equation

### Define Equation like this:
def integrand(x, a, b):
    return a*x**2 + b


### Create an Equation Class
CCC_model = Equation(integrand)


### Solve Integration
# Please put arguments in order of the function argument defined above
equation_args = (
    2,
    1
   )   ## Take all arguments from above defined equations
integration_boundary = [0, 1]  # use +inf for infinity

sol = CCC_model.solve_integration(integration_boundary, equation_args)
print(sol)