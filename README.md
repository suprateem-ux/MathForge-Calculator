# MathForge-Calculator
A calculator made to solve advanced maths like calculus , taylor series etc
If udk how to use github , just open a folder and create a file named calculate.py and paste the calculate.py u see here and use terminal in that directory only ...(where u will run the pip commands and etc) 
# How to input expressions . 
How to Input Expressions (Syntax Guide)
Because Python parses text input literally, math must be typed out using computer syntax rather than standard written notation.
Here is a quick cheat sheet on how to input your equations correctly when prompted by the menu:
| Mathematical Notation | What to Type | Example |
| :--- | :--- | :--- |
| **Multiplication** ($3x$) | Use `*` | `3*x` |
| **Exponents** ($x^2$) | Use `**` | `x**2` | (base**exponent)
| **Fractions** ($\frac{x}{y}$) | Use `/` | `x/y` |
| **Square Root** ($\sqrt{x}$) | Use `sqrt()` | `sqrt(x)` |
| **Trigonometry** (sin(x)) | Use `sin()`, `cos()`, `tan()` | `sin(x)` |
| **Natural Log** (ln(x)) | Use `log()` | `log(x)` |
| **Euler's Constant** ($e^x$) | Use `exp()` | `exp(x)` |

---
Also note complex numbers are denoted by j , not i (why ? blame python)
## 🛠️ Prerequisites & Installation

Before running the script, you need Python installed on your computer

### 1. Install Dependencies
Open your terminal or command prompt and run the following command:

```bash
pip install sympy matplotlib
```
### How to run 

```bash
python calculator.py
```
U will see 
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

```

Type the number of the operation you want.

Example:

U want integeation

Choose option: 

```
2

This opens Integration mode.

---


---

# Examples

## Differentiation

Choose/write

```text

1

```

Enter:

```python

x**3 + sin(x)

```

Output:

```python

3*x**2 + cos(x)

```

---

## Integration

Choose:

```text

2

```

Enter:

```python

tan(x)

```

Output:

```python

-log(cos(x))

```

Another example:

```python

x**2

```

Output:

```python

x**3/3

```

---

## Complex Numbers

Choose:

```text

3

```

Example input:

```python

3+4j

```

The calculator can:

- Add

- Subtract

- Multiply

- Divide

- Find modulus

- Find argument

---

## Equation Solver

Choose:

```text

4

```

Enter:

```python

x**2 - 5*x + 6

```

Output:

```python

[2, 3]

```

---

## Matrix Operations

Choose:

```text

5

```

Example matrix input:

```text

Row 1: 1 2

Row 2: 3 4

```

The calculator can find:

- Determinant

- Inverse

- Transpose

- Eigenvalues

---

## Taylor Series

Choose:

```text

6

```

Enter:

```python

sin(x)

```

Output:

```python

x - x**3/6 + x**5/120 + O(x**6)

```

---

## Laplace Transform

Choose:

```text

7

```

Example:

```python

sin(x)

```

---

## Graph Plotting

Choose:

```text

8

```

Enter:

```python

sin(x)

```

A graph window will open.

---

## 3D Graph Plotting

Choose:

```text

9

```

Enter:

```python

x**2 + y**2

```

A 3D graph window will open.

---

## Limits

Choose:

```text

10

```

Example:

```python

sin(x)/x

```

Approaching value:

```python

0

```

---

## Differential Equations

Choose:

```text

11

```

Example:

```python

Derivative(y(x), x) - y(x)

```

---

## Step-by-Step Derivative

Choose:

```text

12

```

Example:

```python

x**2 + sin(x)

```

---

## Scientific Calculator

Choose:

```text

13

```

Example:

```python

2+5*10

```

---

## Polynomial Tools

Choose:

```text

14

```

Example:

```python

x**2 - 5*x + 6

```

The calculator can:

- Expand

- Factor

- Find roots

---

# Common Errors

## Wrong Power Symbol

Wrong:

```python

x^2

```

Correct:

```python

x**2

```

---

## Forgot Brackets

Wrong:

```python

sin x

```

Correct:

```python
sin(x)
```

# Important Notes

Some options may ask questions like:

```text
(y/n)
```

This means:

| Input | Meaning |
|---|---|
| `y` | Yes |
| `n` | No |

---

# Example

During Integration:

```text
Definite integral? (y/n):
```

If you type:

```text
y
```

the calculator will ask for lower and upper limits.

Example:

```text
Lower limit: 0
Upper limit: 1
```

This calculates a definite integral.

∫₀¹ x² dx

---

If you type:

```text
n
```

the calculator performs an indefinite integral.

Example:
∫ x² dx

Output:

```python
x**3/3
```

---

# Another Example

Input:

```python
tan(x)
```

If you choose:

```text
n
```

Output:

```python
-log(cos(x))
```

---

# Simple Rule

| You Want | Type |
|---|---|
| Yes | `y` |
| No | `n` |

Think of it as a tiny computer asking:

```text
yes or no?
```

# IF U WANT TO USE Gui.py 

## 🚀 How to Run

### 1. Install requirements

Make sure you have Python installed, then install dependencies:

```bash

pip install sympy numpy matplotlib

```

Tkinter usually comes preinstalled with Python.

---

### 2. Run the program

```bash

python Gui.py

```

---

## 🧠 How the GUI works

When you run it, a window opens with multiple tabs:

---

# 📊 1. Classic Tools Tab

### ✏️ Differentiate

- Enter expression:  

  `x**2 + sin(y)`

- Choose variable: `x`, `y`, `z`, or `t`

Output:

- Symbolic derivative

---

### ∫ Integrate

- Example input:  

  `x**2`

- Variable: `x`

Output:

- Indefinite integral + C

---

### 📉 Limits

- Example:  

  `sin(x)/x`

- Variable: `x`

- Point: `0`

Output:

- Limit value

---

### 🔢 Matrix Ops

Input format:

```

1 2; 3 4

```

Gives:

- Transpose

- Determinant

- Rank

- Inverse (if possible)

---

### 🧮 Gaussian Elimination

Input:

```

1 2 3; 4 5 6

```

Output:

- RREF form

- Pivot positions

---

### 🧠 Newton-Raphson

Used to find roots of equations:

Steps:

1. Enter function: `x**2 - 2`

2. Initial guess: `1`

3. Iterations: `10`

Output:

- Step-by-step convergence

- Final root approximation

---

# ⚡ 2. Vector Calculus Tab

Input box supports:

### Scalar field:

```

x**2 + y*z

```

### Vector field:

```

[x**2, y, z]

```

---

### 🟢 Gradient (∇f)

Input must be scalar.

Output:

```

[∂f/∂x, ∂f/∂y, ∂f/∂z]

```

---

### 🔵 Divergence (∇·F)

Input:

```

[x**2, y, z]

```

Output:

- Scalar result

---

### 🔴 Curl (∇×F)

Input:

```

[x**2, y, z]

```

Output:

- Vector result

---

# 🌌 3. Plot Tab

### 2D Plot

Input:

```

x**2

```

Shows:

- Graph of y = f(x)

---

### 3D Plot

Input:

```

x**2 + y**2

```

Shows:

- Surface plot

---

# 📜 4. History Tab

- Stores last 200 calculations

- Click “Refresh Logs” to view past results

---

## ⚠️ Input Rules

### ✔ Allowed

- `x**2` (not x^2)

- `sin(x)`, `cos(x)`

- `[x**2, y, z]` for vectors

### ❌ Not allowed

- `x^2` (must use **)

- Missing brackets for vectors

- Non-numeric matrix formatting

---

## 🧩 Tips

- Use `**` for powers

- Use commas in vectors

- Use semicolons in matrices

- Keep expressions symbolic (SymPy style)

---

## 💡 Example Inputs Cheat Sheet

| Feature | Input |

|--------|------|

| Derivative | `x**3 + x` |

| Integral | `x**2` |

| Limit | `sin(x)/x at 0` |

| Vector | `[x**2, y, z]` |

| Matrix | `1 2; 3 4` |

| Plot | `x**2 + 1` |

---
