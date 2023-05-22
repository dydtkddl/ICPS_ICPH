import sympy as sy
def get_ICPS(A,B,C,D):
    T = sy.Symbol("T")
    R = 8.314
    B = B/1000
    C = C/1000000
    D = D*100000
    expr = R*(A/T + B + C*T + D*(T**(-3)))
    return expr
def get_ICPH(A,B,C,D):
    T = sy.Symbol("T")
    R = 8.314
    B = B/1000
    C = C/1000000
    D = D*100000
    expr = R*(A + B*T + C*(T**2) + D*(T**(-2)))
    return expr
def compute_ICPS(expr, T0, T_):
    T = sy.Symbol("T")
    print("ICPS계산")
    value = sy.integrate(expr ,( T, T0 ,T_))
    return value
def compute_ICPH(expr, T0 ,T):
    T = sy.Symbol("T")
    print("ICPH계산")
    value = sy.integrate(expr ,( T, T0 ,T))
    return value




