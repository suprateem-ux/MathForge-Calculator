import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from collections import deque

from sympy import (
    symbols,
    sin,
    cos,
    tan,
    exp,
    log,
    sqrt,
    pi,
    E,
    diff,
    integrate,
    simplify,
    limit,
    sympify,
    Matrix,
    lambdify,
    init_printing,
)

from sympy.plotting import plot, plot3d
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
)

init_printing(use_unicode=True)

x, y, z, t, n_sym = symbols("x y z t n")

GLOBAL_SYMBOLS = {
    "x": x,
    "y": y,
    "z": z,
    "t": t,
    "n": n_sym,
    "sin": sin,
    "cos": cos,
    "tan": tan,
    "exp": exp,
    "log": log,
    "sqrt": sqrt,
    "pi": pi,
    "E": E,
}

history = deque(maxlen=200)


class MathForgeUltimateGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MathForge Ultimate")
        self.root.geometry("850x650")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)

        self.create_classic_tab()
        self.create_vector_tab()
        self.create_plot_tab()
        self.create_history_tab()

    def safe_parse(self, s):
        if not s or not s.strip():
            return None
        try:
            transformations = standard_transformations + (
                implicit_multiplication_application,
            )
            return parse_expr(
                s.strip(),
                local_dict=GLOBAL_SYMBOLS,
                transformations=transformations,
                evaluate=True,
            )
        except Exception as e:
            messagebox.showerror("Parse Error", str(e))
            return None

    def parse_vector(self, s):
        try:
            clean = s.strip().strip("[]()")
            parts = [self.safe_parse(i.strip()) for i in clean.split(",")]
            if None in parts:
                return None
            return parts
        except Exception:
            return None

    def show(self, title, result):
        history.append((title, str(result)))

        top = tk.Toplevel(self.root)
        top.title(title)
        top.geometry("520x420")

        txt = tk.Text(top, font=("Consolas", 11))
        txt.pack(expand=True, fill="both")

        txt.insert("1.0", str(result))
        txt.config(state="disabled")

    def ask(self, msg):
        res = simpledialog.askstring("Input", msg, parent=self.root)
        if res is None:
            raise ValueError("cancel")
        return res

    def ask_float(self, msg):
        return float(self.ask(msg))

    def ask_int(self, msg):
        return int(self.ask(msg))

    def create_classic_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Classic")

        buttons = [
            ("Differentiate", self.diff),
            ("Integrate", self.integrate),
            ("Limits", self.limit),
            ("Newton", self.newton),
            ("Matrix", self.matrix),
            ("Gaussian", self.gauss),
        ]

        for i, (name, func) in enumerate(buttons):
            ttk.Button(tab, text=name, command=self.wrap(func)).grid(
                row=i // 2, column=i % 2, padx=10, pady=10, sticky="nsew"
            )

    def wrap(self, f):
        def inner():
            try:
                f()
            except ValueError:
                pass
            except Exception as e:
                messagebox.showerror("Error", str(e))

        return inner

    def diff(self):
        expr = self.safe_parse(self.ask("Expression:"))
        if expr is None:
            return

        var = GLOBAL_SYMBOLS.get(
            self.ask("Variable:").strip(),
            symbols(self.ask("Variable:").strip()),
        )

        res = diff(expr, var)
        self.show("Derivative", simplify(res))

    def integrate(self):
        expr = self.safe_parse(self.ask("Expression:"))
        if expr is None:
            return

        var = GLOBAL_SYMBOLS.get(
            self.ask("Variable:").strip(),
            symbols(self.ask("Variable:").strip()),
        )

        res = integrate(expr, var)
        self.show("Integral", res)

    def limit(self):
        expr = self.safe_parse(self.ask("Expression:"))
        if expr is None:
            return

        var = GLOBAL_SYMBOLS.get(
            self.ask("Variable:").strip(),
            symbols(self.ask("Variable:").strip()),
        )

        pt = sympify(self.ask("Value:"), locals=GLOBAL_SYMBOLS)
        self.show("Limit", limit(expr, var, pt))

    def newton(self):
        expr = self.safe_parse(self.ask("f(x):"))
        if expr is None:
            return

        f = lambdify(x, expr, "numpy")
        df = lambdify(x, diff(expr, x), "numpy")

        xn = self.ask_float("Initial guess:")
        iters = self.ask_int("Iterations:")

        log = []

        for i in range(iters):
            dfx = df(xn)
            if abs(dfx) < 1e-12:
                break
            xn = xn - f(xn) / dfx
            log.append(f"{i + 1}: {xn}")

        self.show("Newton", "\n".join(log))

    def matrix(self):
        s = self.ask("Matrix:")
        rows = [list(map(sympify, r.split())) for r in s.split(";")]
        A = Matrix(rows)

        out = f"A:\n{A}\n\nTranspose:\n{A.T}"

        if A.shape[0] == A.shape[1]:
            out += f"\nDet: {A.det()}\nRank: {A.rank()}"
            try:
                out += f"\nInv:\n{A.inv()}"
            except Exception:
                out += "\nNot invertible"

        self.show("Matrix", out)

    def gauss(self):
        s = self.ask("Augmented matrix:")
        rows = [list(map(sympify, r.split())) for r in s.split(";")]
        A = Matrix(rows)

        rref, piv = A.rref()
        self.show("RREF", f"{rref}\nPivots: {piv}")

    def create_vector_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Vector")

        self.vec = ttk.Entry(tab, width=50)
        self.vec.pack()

        ttk.Button(tab, text="Grad", command=self.wrap(self.grad)).pack()
        ttk.Button(tab, text="Div", command=self.wrap(self.div)).pack()
        ttk.Button(tab, text="Curl", command=self.wrap(self.curl)).pack()

    def grad(self):
        expr = self.safe_parse(self.vec.get())
        if expr is None:
            return
        res = Matrix([diff(expr, x), diff(expr, y), diff(expr, z)])
        self.show("Gradient", res)

    def div(self):
        v = self.parse_vector(self.vec.get())
        if not v:
            return
        res = diff(v[0], x) + diff(v[1], y) + diff(v[2], z)
        self.show("Divergence", res)

    def curl(self):
        v = self.parse_vector(self.vec.get())
        if not v:
            return

        Fx, Fy, Fz = v
        res = Matrix(
            [
                diff(Fz, y) - diff(Fy, z),
                diff(Fx, z) - diff(Fz, x),
                diff(Fy, x) - diff(Fx, y),
            ]
        )

        self.show("Curl", res)

    def create_plot_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Plots")

        self.p = ttk.Entry(tab)
        self.p.pack()

        ttk.Button(tab, text="2D", command=self.wrap(self.plot_2d)).pack()
        ttk.Button(tab, text="3D", command=self.wrap(self.plot_3d)).pack()

    def plot_2d(self):
        expr = self.safe_parse(self.p.get())
        if expr:
            plot(expr, (x, -10, 10))

    def plot_3d(self):
        expr = self.safe_parse(self.p.get())
        if expr:
            plot3d(expr, (x, -5, 5), (y, -5, 5))

    def create_history_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="History")

        self.txt = tk.Text(tab)
        self.txt.pack(expand=True, fill="both")

        ttk.Button(tab, text="Refresh", command=self.refresh).pack()

    def refresh(self):
        self.txt.delete("1.0", tk.END)
        for i, (a, b) in enumerate(reversed(history)):
            self.txt.insert(tk.END, f"{i}: {a}\n{b}\n\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = MathForgeUltimateGUI(root)
    root.mainloop()
