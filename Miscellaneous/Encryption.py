import hashlib


def modPow(base, exp, mod):
    if exp == 0:
        return 1
    elif exp == 1:
        return base % mod
    elif exp % 2 == 1:
        return (base * modPow(base, exp - 1, mod)) % mod
    else:
        res_2 = modPow(base, exp / 2, mod) % mod
        return (res_2 * res_2) % mod


x = 824
y = 312
g = 3
n = 11

X = modPow(g, x, n)
print("X  =", X)
Y = modPow(g, y, n)
print("Y  =", Y)

k = modPow(Y, x, n)
print("k  =", k)
k_ = modPow(X, y, n)
print("k' =", k_)

res = modPow(g, x * y, n)
print("re =", res)
