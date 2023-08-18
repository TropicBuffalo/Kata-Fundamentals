def get_middle(s):
    x = len(s)
    if x % 2 == 0 :
        print(s[int((x/2)-1)] + s[int(x/2)])
    else : print (s[int(x/2)])
    
get_middle("tes")