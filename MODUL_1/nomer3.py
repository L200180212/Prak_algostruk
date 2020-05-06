##a
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
    
##b
def jumlahHurufKonsonan(huruf):
    konsonan = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    b = 0
    hasil = 0
    for i in huruf:
        if i in konsonan:
            b += len(i)
        else:
            b += 0
    hasil = len (huruf), b
    return hasil
