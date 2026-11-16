def anagrams(x,y):
    if x == y:
        return True                     
    return sorted(x) == sorted(y)


