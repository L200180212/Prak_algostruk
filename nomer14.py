def formatRupiah(bilangan):
    a = str (bilangan)
    if len(a) <= 3 :
         return "Rp " + a
    else :
         y = a[-3:]
         z = a[:-3]
         return formatRupiah(z) + "." + y
         print  ("Rp ") + formatRupiah(z) + "." +y
