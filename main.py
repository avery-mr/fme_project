#step 1 binary expansion of exponent
#step 2 create lookup table for values base^i in binary expansion using (x*x)modN of previous entry
#step 3 use values from table to calculate (a1 * a2 * ....)modN
def modulo(a, b):
    q = a//b
    return a - b*q

def dec_to_bin(n):
    if n == 0:
        return "0"
    bin_out = ""
    while n > 0:
        r = modulo(n, 2)
        bin_out = str(r) + bin_out
        n = n//2
    return bin_out

def square_n_mod(base, exp, mod):
    bin_exp = dec_to_bin(exp)
    #print(bin_exp)
    k_1 = modulo(base, mod)
    table = [k_1]
    i = 1
    while i < len(bin_exp):
        k_i = modulo(k_1 * k_1, mod)
        table.append(k_i)
        k_1 = k_i
        i+=1

    ret = 1
    table_pos = 0
    for i in bin_exp[::-1]:
        if i == "1":
            ret = ret * table[table_pos]
        table_pos+=1

    return modulo(ret, mod)


def sriramFME(a, n, b):
    result = 1
    square = a
    while n > 0:
        k = n % 2
        if k == 1:
            result = (result * square) % b
        square = (square ** 2) % b
        n //= 2
    return result

print("Format: Base^Exp % Mod")
base = int(input("Base: "))
exp = int(input("Exp: "))
mod = int(input("Mod: "))

print("FME Square n Mod: ")
print(square_n_mod(base, exp, mod))

print("FME Sriram:")
print(sriramFME(base, exp, mod))