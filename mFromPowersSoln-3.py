from sympy import gcd, mod_inverse

def mFromPowers(N, e, f, me, mf):
   
    if gcd(e, f) != 1:
        return None

    x = mod_inverse(e, f)
    y = (1 - e*x) // f


    mx = pow(me, x, N)
    my = pow(mf, y, N)

    m = (mx * my) % N
    return m