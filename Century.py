def century(year):
    year = str(year)
    yearlen = len(year)
    lasttwo = f"{year[-2]}{year[-1]}"
    firsttwo = f"{year[0]}{year[1]}"

    if yearlen == 2 or year == "100":
        return(1)
    elif yearlen == 3:
        if lasttwo == "00" : return int(year[0])
        else :return(int(year[0])+1)
    else :
        if lasttwo == "00" : return int(firsttwo)
        else : return(int(year[0]+year[1])+1)


century(999)