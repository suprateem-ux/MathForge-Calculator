import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from sympy import *
from sympy.plotting import plot, plot3d, plot_parametric, plot_implicit
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
import numpy as np
import matplotlib.pyplot as plt
import cmath
import math
from collections import deque

# =========================================================
# INIT
# =========================================================

init_printing(use_unicode=True)

# Define globally shared mathematical symbols
x, y, z, t, n_sym = symbols("x y z t n")

# Global symbol mapping dictionary for parsing consistency
GLOBAL_SYMBOLS = {
    "x": x, "y": y, "z": z, "t": t, "n": n_sym,
    "sin": sin, "cos": cos, "tan": tan,
    "exp": exp, "log": log, "sqrt": sqrt,
    "pi": pi, "E": E
}

history = deque(maxlen=200)

# =========================================================
# MAIN APP
# =========================================================

class MathForgeUltimateGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("MathForge Ultimate ⚡🌌")
        self.root.geometry("850x650")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)

        self.create_classic_tab()
        self.create_vector_tab()
        self.create_plot_tab()
        self.create_history_tab()

    # =====================================================
    # SAFE PARSER (FIXED MULTI-VARIABLE BUGS)
    # =====================================================

    def safe_parse(self, s):
        if not s or not s.strip():
            return None
        try:
            # Added implicit transformations so users can write "2x" instead of "2*x"
            transformations = standard_transformations + (implicit_multiplication_application,)
            return parse_expr(
                s.strip(),
                local_dict=GLOBAL_SYMBOLS,
                transformations=transformations,
                evaluate=True
            )
        except Exception as e:
            messagebox.showerror("Parse Error", f"Could not parse expression:\n{e}")
            return None

    # =====================================================
    # VECTOR PARSER FIX
    # =====================================================

    def parse_vector(self, s):
        try:
            clean_s = s.strip().strip("[]()")
            components = [self.safe_parse(i.strip()) for i in clean_s.split(",")]
            if None in components:
                return None
            return components
        except Exception:
            return None

    # =====================================================
    # OUTPUT WINDOW
    # =====================================================

    def show(self, title, result):
        history.append((title, str(result)))

        top = tk.Toplevel(self.root)
        top.title(title)
        top.geometry("520x420")

        txt = tk.Text(top, font=("Consolas", 11), wrap="word")
        txt.pack(expand=True, fill="both", padx=10, pady=10)

        txt.insert("1.0", str(result))
        txt.config(state="disabled")

    # =====================================================
    # INPUT HELPER
    # =====================================================

    def ask(self, msg):
        res = simpledialog.askstring("Input Needed", msg, parent=self.root)
        if res is None:
            raise ValueError("cancel")
        return res

    def ask_float(self, msg):
        return float(self.ask(msg))

    def ask_int(self, msg):
        return int(self.ask(msg))

    # =====================================================
    # CLASSIC TAB
    # =====================================================

    def create_classic_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Classic Tools ⚡")

        # Explicitly configure grid rows/columns for proportional resizing
        tab.columnconfigure(0, weight=1)
        tab.columnconfigure(1, weight=1)

        buttons = [
            ("Differentiate", self.diff),
            ("Integrate", self.integrate),
            ("Newton-Raphson", self.newton),
            ("Matrix Ops", self.matrix),
            ("Gaussian Elimination", self.gauss),
            ("Limits", self.limit),
        ]

        for i, (t, f) in enumerate(buttons):
            row = i // 2
            col = i % 2
            tab.rowconfigure(row, weight=1)
            btn = ttk.Button(tab, text=t, command=self.safe_wrap(f))
            btn.grid(row=row, column=col, padx=15, pady=15, sticky="nsew")

    def safe_wrap(self, func):
        def wrapper():
            try:
                func()
            except ValueError:
                pass  # Handles user cancellation smoothly
            except Exception as e:
                messagebox.showerror("Execution Error", str(e))
        return wrapper

    def diff(self):
        expr = self.safe_parse(self.ask("Enter expression (e.g., x**2 + sin(y)):"))
        if expr is None: return
        
        var_str = self.ask("Differentiate with respect to variable (x, y, z, or t):").strip()
        # Look up the system's core pre-defined symbol reference
        var = GLOBAL_SYMBOLS.get(var_str, symbols(var_str))
        
        res = diff(expr, var)
        self.show("Derivative", f"d/d{var} ({expr}) =\n\n{simplify(res)}")

    def integrate(self):
        expr = self.safe_parse(self.ask("Enter expression to integrate:"))
        if expr is None: return
        
        var_str = self.ask("Integrate with respect to variable (x, y, z, or t):").strip()
        var = GLOBAL_SYMBOLS.get(var_str, symbols(var_str))
        
        res = integrate(expr, var)
        self.show("Symbolic Integral", f"∫ ({expr}) d{var} =\n\n{res} + C")

    def limit(self):
        expr = self.safe_parse(self.ask("Enter expression:"))
        if expr is None: return
        
        var_str = self.ask("Limit variable (x, y, z, t):").strip()
        var = GLOBAL_SYMBOLS.get(var_str, symbols(var_str))
        
        pt = sympify(self.ask("Approaching value (e.g., 0, oo):"), locals=GLOBAL_SYMBOLS)
        self.show("Limit Evaluation", f"lim [{var} → {pt}] ({expr}) =\n\n{limit(expr, var, pt)}")


    def newton(self):
        expr = self.safe_parse(self.ask("Enter function f(x):"))
        if expr is None: return

        f = lambdify(x, expr, "numpy")
        df = lambdify(x, diff(expr, x), "numpy")

        xn = self.ask_float("Initial guess:")
        iters = self.ask_int("Max iterations:")

        log = [f"Function: {expr}", f"Initial Guess: {xn}\n" + "="*30]

        for i in range(iters):
            try:
                dfx = df(xn)
                if abs(dfx) < 1e-12:
                    log.append(f"Iteration {i+1}: Derivative too close to zero ({dfx:.2e}) → Exploded/Stopped.")
                    break

                xn1 = xn - f(xn) / dfx

                if not np.isfinite(xn1):
                    log.append(f"Iteration {i+1}: Numerical divergence encountered → Stopped.")
                    break

                xn = xn1
                log.append(f"Iteration {i+1}: x = {xn}")
                
            except Exception as e:
                log.append(f"Error during execution: {e}")
                break

        log.append("="*30 + f"\nFinal Approximate Root ≈ {xn}")
        self.show("Newton-Raphson Trace Engine", "\n".join(log))

    # =====================================================
    # MATRIX CALCULATOR
    # =====================================================

    def matrix(self):
        s = self.ask("Enter matrix rows separated by ';' and columns by spaces\nExample: 1 2; 3 4")
        rows = [list(map(sympify, r.split())) for r in s.split(";")]
        A = Matrix(rows)

        out = f"Input Matrix A:\n{A}\n\nTranspose Aᵀ:\n{A.T}"

        if A.shape[0] == A.shape[1]:
            out += f"\n\nDeterminant: {A.det()}\nRank: {A.rank()}"
            try:
                out += f"\nInverse A⁻¹:\n{A.inv()}"
            except:
                out += f"\nInverse A⁻¹: Matrix is singular (non-invertible)."

        self.show("Matrix Structural Matrix Output", out)

    def gauss(self):
        s = self.ask("Enter Augmented Matrix (e.g., 1 2 3; 4 5 6):")
        rows = [list(map(sympify, r.split())) for r in s.split(";")]
        A = Matrix(rows)

        rref, piv = A.rref()
        self.show("Gaussian Elimination (RREF)", f"Original Augmented Matrix:\n{A}\n\nReduced Row Echelon Form:\n{rref}\n\nPivot Column Indices: {piv}")

    # =====================================================
    # VECTOR TAB (FIXED SCALAR / VECTOR OPERATORS)
    # =====================================================

    def create_vector_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Vector Calculus ⚡")

        lbl = ttk.Label(tab, text="Vector Field [Fx, Fy, Fz] OR Scalar Function f(x,y,z):", font=("Arial", 11, "bold"))
        lbl.pack(pady=10)

        self.vec = ttk.Entry(tab, width=50, font=("Consolas", 11))
        self.vec.pack(pady=5)
        
        lbl_info = ttk.Label(tab, text="For vector fields use brackets: [x**2, y, z]\nFor scalar functions enter terms directly: x**2 + y*z")
        lbl_info.pack(pady=5)

        btn_frame = ttk.Frame(tab)
        btn_frame.pack(pady=15)

        ttk.Button(btn_frame, text="Gradient (of Scalar Input)", command=self.safe_wrap(self.grad)).grid(row=0, column=0, padx=10, pady=5)
        ttk.Button(btn_frame, text="Divergence (of Vector Field Input)", command=self.safe_wrap(self.div)).grid(row=0, column=1, padx=10, pady=5)
        ttk.Button(btn_frame, text="Curl (of Vector Field Input)", command=self.safe_wrap(self.curl)).grid(row=1, column=0, padx=10, pady=5)

    def grad(self):
        # Gradient handles an individual scalar expression, not a split bracket vector list.
        expr = self.safe_parse(self.vec.get())
        if expr is None or isinstance(expr, list):
            messagebox.showerror("Input Error", "Gradient inputs must be scalar expressions (e.g., x**2 * y * z)")
            return

        res = Matrix([diff(expr, var) for var in (x, y, z)])
        self.show(f"Gradient Field ∇({expr})", res)

    def div(self):
        v = self.parse_vector(self.vec.get())
        if not v or len(v) != 3:
            messagebox.showerror("Input Error", "Divergence requires a 3-component vector field expression: [Fx, Fy, Fz]")
            return

        res = diff(v[0], x) + diff(v[1], y) + diff(v[2], z)
        self.show("Divergence ∇·F", f"div(F) = {res}")

    def curl(self):
        v = self.parse_vector(self.vec.get())
        if not v or len(v) != 3:
            messagebox.showerror("Input Error", "Curl requires a 3-component vector field expression: [Fx, Fy, Fz]")
            return

        Fx, Fy, Fz = v
        curl_res = Matrix([
            diff(Fz, y) - diff(Fy, z),
            diff(Fx, z) - diff(Fz, x),
            diff(Fy, x) - diff(Fx, y)
        ])
        self.show("Curl ∇×F", curl_res)

    # =====================================================
    # ADVANCED PLOTS (ADDED MULTI-FUNCTION PLOTTING)
    # =====================================================

    def create_plot_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Plots 🌌")

        ttk.Label(tab, text="Enter Cartesian Equation f(x) or Multi-Variable f(x, y):", font=("Arial", 10, "bold")).pack(pady=10)

        self.p = ttk.Entry(tab, width=40, font=("Consolas", 11))
        self.p.pack(pady=5)

        btn_frame = ttk.Frame(tab)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Plot 2D Line Graph", command=self.safe_wrap(self.plot_2d)).grid(row=0, column=0, padx=5)
        ttk.Button(btn_frame, text="Plot 3D Surface Graph", command=self.safe_wrap(self.plot_3d)).grid(row=0, column=1, padx=5)

    def plot_2d(self):
        expr = self.safe_parse(self.p.get())
        if expr:
            plot(expr, (x, -10, 10), title=f"2D Plot: f(x) = {expr}")

    def plot_3d(self):
        expr = self.safe_parse(self.p.get())
        if expr:
            plot3d(expr, (x, -5, 5), (y, -5, 5), title=f"3D Surface Plot: z = {expr}")

    # =====================================================
    # HISTORY TAB
    # =====================================================

    def create_history_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Calculation History")

        self.txt = tk.Text(tab, font=("Consolas", 10))
        self.txt.pack(expand=True, fill="both", padx=10, pady=10)

        ttk.Button(tab, text="Refresh Logs", command=self.refresh).pack(pady=5)

    def refresh(self):
        self.txt.config(state="normal")
        self.txt.delete("1.0", tk.END)
        if not history:
            self.txt.insert(tk.END, "No records found in current app lifecycle.")
        for i, (a, b) in enumerate(reversed(history), 1):
            self.txt.insert(tk.END, f"[{i}] {a}\nOutput:\n{b}\n" + "-"*50 + "\n\n")
        self.txt.config(state="disabled")


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = MathForgeUltimateGUI(root)
    root.mainloop()
