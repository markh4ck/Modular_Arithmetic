p = 11

ints = [
3,5,4
]

def legendre_symbol(a, p):
    return pow(a, (p - 1) // 2, p) 

def sqrt_mod_p(a, p):
    return pow(a, (p + 1) // 4, p)

for a in ints:
    leg = legendre_symbol(a, p)
    if leg == 1:
        root = sqrt_mod_p(a, p)
        root2 = p - root
        print(f"Residuo cuadrático encontrado a={a}")
        print(f"Raíces: {root} y {root2}")
        print(f"Raíz mayor (flag): {max(root, root2)}\n")
    elif leg == 0:
        print(f"a={a} es 0 \n")
    else:
        print(f"a={a} no es residuo cuadrático mod p, sin raíz.\n")
