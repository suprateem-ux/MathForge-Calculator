from sympy import (
    Matrix,
    Function,
    arg,
    diff,
    dsolve,
    expand,
    factor,
    init_printing,
    integrate,
    laplace_transform,
    limit,
    pprint,
    series,
    solve,
    symbols,
    sympify,
)

from sympy.plotting import plot, plot3d
import matplotlib.pyplot as plt

init_printing(use_unicode=True)

x, y, z = symbols("x y z")

def differentiate():

    expr = sympify(input("Enter expression: "))

    print("\nDerivative:")
    pprint(diff(expr, x)

def integrate_expr():

    expr = sympify(input("Enter expression: "))

    choice = input("Definite integral? (y/n): ")

    if choice.lower() == "y":

        a = float(input("Lower limit: "))
        b = float(input("Upper limit: "))

        result = integrate(expr, (x, a, b))

    else:
        result = integrate(expr, x)

    print("\nIntegral:")
    pprint(result)

def complex_numbers():

    a = complex(input("Enter first complex number: "))
    b = complex(input("Enter second complex number: "))

    print("\nAddition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)

    print("\nModulus:", abs(a))
    print("Argument:", arg(a))

def equation_solver():

    expr = sympify(input("Enter equation equal to 0: "))

    result = solve(expr, x)

    print("\nSolutions:")
    pprint(result)

def matrix_operations():

    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix_data = []

    for i in range(rows):

        row = list(map(int, input(f"Row {i + 1}: ").split()))
        matrix_data.append(row)

    A = Matrix(matrix_data)

    print("\nMatrix:")
    pprint(A)

    if rows == cols:

        print("\nDeterminant:")
        pprint(A.det())

        try:
            print("\nInverse:")
            pprint(A.inv())

        except Exception:
            print("Matrix has no inverse.")

    print("\nTranspose:")
    pprint(A.T)

    print("\nEigenvalues:")
    pprint(A.eigenvals())

def taylor_series():

    expr = sympify(input("Enter expression: "))

    n = int(input("Enter order: "))

    result = series(expr, x, 0, n)

    print("\nTaylor Series:")
    pprint(result)

def laplace_transform_calc():

    expr = sympify(input("Enter expression: "))

    s = symbols("s")

    result = laplace_transform(expr, x, s)

    print("\nLaplace Transform:")
    pprint(result)

def graph_plot():

    expr = sympify(input("Enter expression in x: "))

    print("\nOpening graph window...")

    plot(expr)

def graph_3d():

    expr = sympify(input("Enter expression in x and y: "))

    print("\nOpening 3D graph...")

    plot3d(expr)

def limits_calc():

    expr = sympify(input("Enter expression: "))

    point = sympify(input("Approaching value: "))

    result = limit(expr, x, point)

    print("\nLimit:")
    pprint(result)

def differential_equation():

    Function("y")

    expr = sympify(input(
        "Enter differential equation using y(x): "
    ))

    result = dsolve(expr)

    print("\nSolution:")
    pprint(result)

def derivative_steps():

    expr = sympify(input("Enter expression: "))

    print("\nExpression:")
    pprint(expr)

    print("\nStep 1: Identify function")

    print("\nStep 2: Differentiate")

    result = diff(expr, x)

    pprint(result)

def scientific_calc():

    expr = input("Enter calculation: ")

    result = eval(expr)

    print("\nAnswer:", result)

def polynomial_tools():

    expr = sympify(input("Enter polynomial: "))

    print("\nExpanded Form:")
    pprint(expand(expr))

    print("\nFactored Form:")
    pprint(factor(expr))

    print("\nRoots:")
    pprint(solve(expr, x))

def menu():

    while True:

        print("""
========================================
          MATHFORGE CALCULATOR
========================================

1. Differentiation
2. Integration
3. Complex Numbers
4. Equation Solver
5. Matrix Operations
6. Taylor Series
7. Laplace Transform
8. Graph Plotting
9. 3D Graph Plotting
10. Limits
11. Differential Equations
12. Step-by-Step Derivative
13. Scientific Calculator
14. Polynomial Tools
15. Exit
""")

        choice = input("Choose option: ")

        if choice == "1":
            differentiate()

        elif choice == "2":
            integrate_expr()

        elif choice == "3":
            complex_numbers()

        elif choice == "4":
            equation_solver()

        elif choice == "5":
            matrix_operations()

        elif choice == "6":
            taylor_series()

        elif choice == "7":
            laplace_transform_calc()

        elif choice == "8":
            graph_plot()

        elif choice == "9":
            graph_3d()

        elif choice == "10":
            limits_calc()

        elif choice == "11":
            differential_equation()

        elif choice == "12":
            derivative_steps()

        elif choice == "13":
            scientific_calc()

        elif choice == "14":
            polynomial_tools()

        elif choice == "15":

            print("Exiting MathForge...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    menu()
