def katakan(bilangan):
    angka=["","Satu","Dua","Tiga","Empat","Lima","Enam","Tujuh",
           "Delapan","Sembilan","Sepuluh","Sebelas"]
    Hasil = " "
    n = int(bilangan)
    if n>=0 and n<=11:
        Hasil = Hasil +angka[n]
    elif n<20:
        Hasil = katakan(n % 10) + " Belas"
    elif n<100:
        Hasil = katakan(n / 10) + " Puluh" + katakan(n%10)
    elif n<200:
        Hasil = " Seratus" + katakan(n-100)
    elif n<1000:
        Hasil = katakan(n/100) + " Ratus" + katakan(n%100)
    elif n<2000:
        Hasil = " Seribu" + katakan(n-1000)
    elif n<10000:
        Hasil = katakan(n/1000) + " Ribu" + katakan(n%1000)
    elif n<20000:
        Hasil = " Sepuluh Ribu" + katakan(n-10000)
    elif n<100000:
        Hasil = katakan(n/10000) + " Puluh" + katakan(n%10000)
    elif n<200000:
        Hasil = " Seratus Ribu" + katakan(n-100000)
    elif n<1000000:
        Hasil = katakan(n/100000) + " Ratus" + katakan(n%100000)
    elif n<2000000:
        Hasil = " Satu Juta" + katakan(n-1000000)
    elif n<10000000:
        Hasil = katakan(n/1000000) + " Juta" + katakan(n%1000000)
    elif n==10000000:
        Hasil = "Satu Milyar" + katakan(n%10000000)
    else:
        Hasil = "Angka Hanya Sampai Satu Milyar"
    return Hasil
