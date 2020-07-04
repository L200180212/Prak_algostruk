class Pesan(object):
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print("kalimatku mempunyai", len(self.teks), "karakter.")
    def perbarui(self, stringBaru):
        self.teks = stringBaru


#A
    def apakahTerkandung(self,a):
        if a in self.teks:
            return True
        else:
            return False
#B
    def hitungKonsonan(self):
        kon=0
        x=self.teks
        alfaKon="QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm"
        for i in x:
            if i in alfaKon:
                kon +=1
        return kon

#C
    def hitungVokal(self):
        voc=0
        x=self.teks
        alfaVoc="aiueoAIUEO"
        for i in x:
            if i in alfaVoc:
                voc +=1
        return voc
#Nomer2
class Manusia(object):
    keadaan = "lapar"
    def __init__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salaaaam, Namaku ", self.nama)
    def makan(self, s):
        print ("Saya baru saja makan ", s)
        self.keadaan = "kenyang"
    def olahraga(self, k):
        print ("Saya baru saja latihan ", k)
        self.keadaan = "lapar"
    def mengalikanDenganDua(self,n):
        return n*2


class Mahasiswa (Manusia):
    def __init__ (self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__ (self):
        s = self.nama + ", NIM " +str(self.NIM) \
            + ". Tinggal di " + self.kotaTinggal \
            + ". Uang saku Rp " + str(self.uangSaku) \
            + " tiap bulannya."
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        print("Saya baru saja makan", s, "sambil belajar.")
        self.keadaan = "kenyang"

#A
    def ambilKotaTinggal(self):
        return self.kotaTinggal
#B
    def perbaruiKotaTinggal(self, ubah):
        self.kotaTinggal=ubah
#C
    def tambahUangSaku(self, tambah):
        self.uangSaku+=tambah

#Nomer3
class Manusia(object):
    keadaan = "lapar"
    def __init__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salaaaam, Namaku ", self.nama)
    def makan(self, s):
        print ("Saya baru saja makan ", s)
        self.keadaan = "kenyang"
    def olahraga(self, k):
        print ("Saya baru saja latihan ", k)
        self.keadaan = "lapar"
    def mengalikanDenganDua(self,n):
        return n*2


class Mahasiswa (Manusia):
    def __init__ (self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__ (self):
        s = self.nama + ", NIM " +str(self.NIM) \
            + ". Tinggal di " + self.kotaTinggal \
            + ". Uang saku Rp " + str(self.uangSaku) \
            + " tiap bulannya."
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        print("Saya baru saja makan", s, "sambil belajar.")
        self.keadaan = "kenyang"

    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self, ubah):
        self.kotaTinggal=ubah
    def tambahUangSaku(self, tambah):
        self.uangSaku += tambah
        
print("Masukkan Data mahasiswa Di Sini : ")
a=raw_input("Nama      : ")
b=raw_input("NIM       : ")
c=raw_input("Asal      : ")
d=raw_input("Uang Saku : ")
maha=Mahasiswa(a,b,c,d)

#Nomer4&5
class Manusia(object):
    keadaan = "lapar"
    def __init__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salaaaam, Namaku ", self.nama)
    def makan(self, s):
        print ("Saya baru saja makan ", s)
        self.keadaan = "kenyang"
    def olahraga(self, k):
        print ("Saya baru saja latihan ", k)
        self.keadaan = "lapar"
    def mengalikanDenganDua(self,n):
        return n*2


class Mahasiswa (Manusia):
    def __init__ (self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__ (self):
        s = self.nama + ", NIM " +str(self.NIM) \
            + ". Tinggal di " + self.kotaTinggal \
            + ". Uang saku Rp " + str(self.uangSaku) \
            + " tiap bulannya."
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        print("Saya baru saja makan", s, "sambil belajar.")
        self.keadaan = "kenyang"

    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self, ubah):
        self.kotaTinggal=ubah
    def tambahUangSaku(self, tambah):
        self.uangSaku += tambah

    listKuliah=[]
    def ambilKuliah(self, kuliah):
        self.listKuliah.append(kuliah)
    def hapusKuliah(self, hapus):
        self.listKuliah.remove(hapus)

#Nomer6
class Manusia(object):
    keadaan = "lapar"
    def __init__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salaaaam, Namaku ", self.nama)
    def makan(self, s):
        print ("Saya baru saja makan ", s)
        self.keadaan = "kenyang"
    def olahraga(self, k):
        print ("Saya baru saja latihan ", k)
        self.keadaan = "lapar"
    def mengalikanDenganDua(self,n):
        return n*2


class Mahasiswa (Manusia):
    def __init__ (self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__ (self):
        s = self.nama + ", NIM " +str(self.NIM) \
            + ". Tinggal di " + self.kotaTinggal \
            + ". Uang saku Rp " + str(self.uangSaku) \
            + " tiap bulannya."
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        print("Saya baru saja makan", s, "sambil belajar.")
        self.keadaan = "kenyang"

    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self, ubah):
        self.kotaTinggal=ubah
    def tambahUangSaku(self, tambah):
        self.uangSaku += tambah
    listKuliah=[]
    def ambilKuliah(self, kuliah):
        self.listKuliah.append(kuliah)
    def hapusKuliah(self, hapus):
        self.listKuliah.remove(hapus)

class SiswaSMA(Manusia):
    def __init__(self, nama, NISN, uangSaku, alamat):
        self.nama=nama
        self.nisn=NISN
        self.uangSaku=uangSaku
        self.alamat=alamat
    def __str__(self):
        a='Nama : ' + str(self.nama) + '\n' \
           + 'NISN : ' + str(self.nisn) + '\n' \
           + 'Alamat : ' + str(self.alamat) + '\n' \
           + 'Uang Saku : ' + str(self.uangSaku)
        return a
