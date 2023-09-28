def descending_order(num):
    res = [str(x) for x in str(num)]
    res.sort(reverse=True)
    number = int("".join(res))
    #return number
    print(number)

descending_order(1234)