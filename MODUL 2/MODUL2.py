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
