
#reverse function

def my_reverse(l):
    output = []
    count = len(l)-1
    while count >= 0:
        output.append(l[count])
        count = count - 1
    return output
