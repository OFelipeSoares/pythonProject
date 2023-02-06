def Fatorial(n):
    if (n == 1) or (n == 0):
        return 1
    else:
        return Fatorial(n-1)*n
print(Fatorial(4))