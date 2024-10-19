# Final solution, I could've saved me soo much time ... especially in stack frames for the reursion ...
def solution(xs):
    if len(xs) == 1:
        return str(xs[0])
    min_neg = None
    zeroes = 0
    negs = 0

    prod = 1
    for i in range(len(xs)):
        if xs[i] == 0:
            zeroes += 1
        elif xs[i] < 0:
            negs += 1
            if min_neg == None:
                min_neg = xs[i]
            min_neg = max(xs[i], min_neg)
            prod *= xs[i]
        else:
            prod *= xs[i]

    if negs == 1 and zeroes != 0:
        return str(0)
    
    if negs % 2 != 0:
        prod = int(prod / min_neg)
    
    return str(prod)
