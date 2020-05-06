def apakahTerkandung(x,y):
    a=True
    for i in range(len(y)):
        if x in y:
            a=True
        else:
            a=False
    return a
