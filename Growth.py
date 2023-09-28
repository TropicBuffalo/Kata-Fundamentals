def nb_year(p0, percent, aug, p):
    inhabs = p0
    count = 0
    while p >= inhabs :
        inhabs = inhabs + int(inhabs * (percent/100)) + aug
        count = count + 1
    
    print(count)

nb_year(1500, 5, 100, 5000)