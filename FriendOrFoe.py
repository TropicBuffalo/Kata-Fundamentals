def friend(y):
    newlist = []

    for x in y:
        if len(x)==4:
            newlist.append(x)

    print(newlist)

friend(["apple", "banana", "cherry", "kiwi", "mango"])
