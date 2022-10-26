from sympy import *

def derivative(f, x):
    h = 0.001
    return (f(x+h) -f(x)) / h

init_printing()
x, y = symbols('x,y')

fx = x**3 - 3*x**2
fpx = diff(fx, x)
fppx = diff(fpx, x)
fpppx = diff(fppx, x)

p = plot(fx, fpx, fppx, fpppx, (x, -5, 5), ylim=(-10, 10), legend=True, xlabel='x', ylabel='f(x)', show=False)
p[0].label = f"f(x) = {fx} [Position]"
p[1].label = f"f'(x) = {fpx} [Velocity]"
p[2].label = f"f''(x) = {fppx} [Acceleration]"
p[3].label = f"f'''(x) = {fpppx} [Jerk]"

p.show()