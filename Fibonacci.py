

def big_fibonacci(n):
    k = 1
    l = 1
    while n > len(str(l)):
        m = k + l
        k = l
        l = m
    return l



