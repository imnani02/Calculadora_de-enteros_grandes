def multiplicar(u, v):
    if u < 10 or v < 10:
        return u * v

    n = max(len(str(u)), len(str(v)))
    s = n // 2

    w = u // (10 ** s)
    x = u % (10 ** s)

    y = v // (10 ** s)
    z = v % (10 ** s)

    resultado = (multiplicar(w, y) * (10 ** (2 * s))) \
                + ((multiplicar(w, z) + multiplicar(x, y)) * (10 ** s)) \
                + multiplicar(x, z)

    return resultado


u = int(input("Ingrese el primer número: "))
v = int(input("Ingrese el segundo número: "))

resultado = multiplicar(u, v)

print("Resultado:", resultado)