def is_prime(n):
    for s in range(2, n):
        if n % s == 0:
            return False
    
    return True
#True returns when the for loop is done 