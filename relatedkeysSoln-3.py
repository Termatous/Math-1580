from sympy import mod_inverse

def decrypt_elgamal(c1, c2, p, a, k):
    s = pow(c1, a, p)
    s_inv = mod_inverse(s, p)
    m = (c2 * s_inv) % p
    return m

def relatedkeys(g, p, A, c11, c12, m1, c21, c22):
    k1 = (c12 * mod_inverse(m1, p)) % p
    for u in range(1, 101):
        for v in range(1, 101):
            k2 = (u * k1 + v) % p
            s = pow(A, k2, p)
            s_inv = mod_inverse(s, p)
            m2 = (c22 * s_inv) % p
            if (pow(g, k2, p) == c21) and ((m2 * s) % p == c22):
                return m2
            
    return None