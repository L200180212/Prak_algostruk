##Membuat kelas MhsTIF
class MhsTIF(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku
        
c0 = MhsTIF("Ika", 10, "Sukoharjo", 240000)
c1 = MhsTIF("Budi", 51, "Sragen", 230000)
c2 = MhsTIF("Ahmad", 2, "Surakarta", 250000)
c3 = MhsTIF("Chandra", 18, "Surakarta", 235000)
c4 = MhsTIF("Eka", 4, "Boyolali", 240000)
c5 = MhsTIF("Fandi", 31, "Salatiga", 250000)
c6 = MhsTIF("Deni", 13, "Klaten", 245000)
c7 = MhsTIF("Galuh", 5, "Wonogiri", 245000)
c8 = MhsTIF("Janto", 23, "Klaten", 245000)
c9 = MhsTIF("Hasan", 64, "Karanganyar", 270000)
c10 = MhsTIF("Khalid", 29, "Purwodadi", 265000)


Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

#Nomer 1
def cariKotaTinggal(list, target):
    a = []
    for i in list :
        if i.kotaTinggal == target:
            a.append(list.index(i))
    return a
#Nomer 2
def cariUangSakuTerkecil(list):
    temp = list[0].uangSaku
    for i in list[1:]:
        if i.uangSaku < temp:
            temp = i.uangSaku
    return temp
#Nomer 3
def cariUangSakuTerkecilObject(list):
    temp = list[0].uangSaku
    obj = list[0].nama
    for i in list[1:]:
        if i.uangSaku < temp:
            temp = i.uangSaku
            obj = i.nama
        elif i.uangSaku == temp:
            temp.append(i)
            obj.append(i)
    return obj

# Nomer 4
def cariUangSakuKurang250k(list):
    temp = []
    for i in list:
        if i.uangSaku < 250000:
            temp.append(i)
    return temp

a=cariUangSakuKurang250k(Daftar)
for i in a:
    print(i.nama)

# Nomer 5
class node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    def cariLinkedList(self, dicari):
        curNode = self
        while curNode is not None:
            if curNode.next != None:
                if curNode.data != dicari:
                    curNode = curNode.next
                else:
                    print("Data", dicari, "ada dalam linked list")
                    break
            elif curNode.next == None:
                print ("Data", dicari, "tidak ada dalam linked list")
                break

# Nomer 6
def binSe(kumpulan, target):
    low = 0
    high = len(kumpulan)-1
    while low <= high:
        mid = (high+low)//2
        if kumpulan[mid] == target:
            return mid
        elif target < kumpulan[mid]:
            high = mid-1
        else:
            low = mid+1
        return False
#cara
kumpulan = [2,4,5,10,13,18,23,29,31,51,64]
print(binSe(kumpulan, 3))

#Nomer 7

def binSeAll(kumpulan, target):
    temp = []
    low = 0
    high = len(kumpulan)-1
    while low <= high :
        mid = (high+low)//2
        if kumpulan[mid] == target:
            midKiri = mid-1
            while kumpulan[midKiri] == target:
                temp.append(midKiri)
                midKiri = midKiri-1
            temp.append(mid)
            midKanan = mid+1
            while kumpulan[midKanan] == target:
                temp.append(midKanan)
                midKanan = midKanan+1
            return temp
        elif target < kumpulan[mid]:
            high = mid-1
        else:
            low = mid+1
    return False

kumpulan = [2,3,5,6,6,6,8,9,9,10,11,12,13,13,14]
print(binSeAll(kumpulan, 6))
