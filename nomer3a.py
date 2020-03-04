def jumlahHurufVokal(huruf):
    vokal= "AIUEOaiueo"
    a=0
    hasil=0
    for i in huruf:
        if i in vokal:
            a += len(i)
        else:
            a += 0
    hasil = len (huruf),a
    return hasil
