# 1).

def popular_words(string, pop_word):
    dict = {}
    string = string.lower()
    string = "".join(string)
    string = string.replace(" ", "")
    for i in pop_word:
        dict[i] = string.count(i)
    return dict


print(popular_words("Who are you and whats your name", ["y", "e"]))


# 2).

def max_min(spis):
    if spis == ():
        print(0)
    else:
        print(round(max(spis) - min(spis), 2))


max_min((1, 4, 6, 4, 7, 4, 2, 9, -2, 44, 2, 3))
