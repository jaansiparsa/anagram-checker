LASTNAME = "Parsa"

def anagram(words):
    list = words.split("|")
    w1 = list[0]
    w2 = list[1]
    w1List = []
    w2List = []
    for i in w1:
        w1List.append(i)
    for i in w2:
        w2List.append(i)
    if w1 == w2:
        return False
    for i in w1List:
        if i in w2List:
            w2List.remove(i)
        else:
            return False
    if w2List == []:
        return True
    else:
        return False

