from sympy import *
from sympy.plotting import plot
import matplotlib.pyplot as plt

init_printing(use_unicode=True)

x, y, z = symbols('x y z')

def differentiate():
    expr = sympify(input("Enter expression: "))

    print("\nDerivative:")
    pprint(diff(expr, x))


def integrate_expr():
    expr = sympify(input("Enter expression: "))

    choice = input("Definite integral? (y/n): ")

    if choice.lower() == 'y':
        a = float(input("Lower limit: "))
        b = float(input("Upper limit: "))

        result = integrate(expr, (x, a, b))

    else:
        result = integrate(expr, x)

    print("\nIntegral:")
    pprint(result)


def complex_numbers():
    a = complex(input("Enter first complex number (example 3+4j): "))
    b = complex(input("Enter second complex number: "))

    print("\nAddition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)

    print("\nModulus of first:", abs(a))
    print("Argument of first:", arg(a))


def equation_solver():
    expr = sympify(input("Enter equation equal to 0: "))

    result = solve(expr, x)

    print("\nSolutions:")
    pprint(result)


def matrix_operations():

    print("\nEnter Matrix A")

    A = Matrix([
        list(map(int, input("Row 1: ").split())),
        list(map(int, input("Row 2: ").split()))
    ])

    print("\nMatrix:")
    pprint(A)

    print("\nDeterminant:")
    pprint(A.det())

    print("\nInverse:")
    pprint(A.inv())


def taylor_series():
    expr = sympify(input("Enter expression: "))

    n = int(input("Enter order: "))

    result = series(expr, x, 0, n)

    print("\nTaylor Series:")
    pprint(result)


def laplace_transform_calc():

    expr = sympify(input("Enter expression: "))

    s = symbols('s')

    result = laplace_transform(expr, x, s)

    print("\nLaplace Transform:")
    pprint(result)


def graph_plot():

    expr = sympify(input("Enter expression in x: "))

    print("\nOpening graph window...")

    plot(expr)


def menu():

    while True:

        print("""
====================================
        MATHFORGE CALCULATOR
====================================

1. Differentiation
2. Integration
3. Complex Numbers
4. Equation Solver
5. Matrix Operations
6. Taylor Series
7. Laplace Transform
8. Graph Plotting
9. Exit
""")

        choice = input("Choose option: ")

        if choice == '1':
            differentiate()

        elif choice == '2':
            integrate_expr()

        elif choice == '3':
            complex_numbers()

        elif choice == '4':
            equation_solver()

        elif choice == '5':
            matrix_operations()

        elif choice == '6':
            taylor_series()

        elif choice == '7':
            laplace_transform_calc()

        elif choice == '8':
            graph_plot()

        elif choice == '9':
            print("Exiting MathForge...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    menu()
