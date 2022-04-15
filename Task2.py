def to_hex(n):
    f = n // 16
    s = n % 16

    l = ["0","1", "2","3","4","5","6","7","8","9","a","b","c","d","e","f"]

    if n < 16:
        return(l[s])
    else:
        return(l[f]+l[s])

#The first part of the task is done
#for the coloring part return zeros

def hex_color(a,b,c):
    af = a // 16
    asl = a % 16
    bf = b // 16
    bs = b % 16
    cf = c // 16
    cs = c % 16

    l = ["0","1", "2","3","4","5","6","7","8","9","a","b","c","d","e","f"]

    return('#'+l[af]+l[asl]+l[bf]+l[bs]+l[cf]+l[cs])


