def dig_pow(n, p):
    digits = [int(d) for d in str(n)]
    total = sum (d** (p + i ) for i, d in enumerate(digits))
    if total % n == 0:
        print(total // n)
    else:
        return -1
    
dig_pow(89, 1)