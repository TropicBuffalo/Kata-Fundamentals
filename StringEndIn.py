def solution(text, ending):
    x = len(ending)
    y = text[-x:]
    if y == ending :
        print (True)
    else :
        print(False)


solution("samurai", "ai")