def banjo(name):
    fname = str(name)
    if fname[0] == 'R' or fname[0] == 'r':
        return fname + " plays banjo"
    else :
        return fname + " does not play banjo"
    

banjo("rkki")