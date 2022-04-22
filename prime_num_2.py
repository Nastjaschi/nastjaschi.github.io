def is_prime(n):
    for s in range(2, n):
        if n % s == 0:
            return False
    
    return True
#True returns when the for loop is done 

def primes_below(m):
    l = []
    for k in range(2, m):
        if is_prime(k) == True:
            l.append(k)
   
    return(l)

#print(primes_below(17))
#print(primes_below(8))