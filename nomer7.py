def faktorPrima(a):
    bilanganList = []
    loop=2
    while loop <= a:
        if a%loop == 0:
            a/=loop
            bilanganList.append(loop)
        else:
            loop+=1
    return bilanganList
