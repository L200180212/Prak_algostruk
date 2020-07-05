#Nomor 1

# NOMER 1

import re
f=open('indonesia.txt','r')
baca = f.read()
f.close()
a=r'me\w+'
kata = re.findall(a,baca)
print(kata)

#Nomer 2

import re
f=open('indonesia.txt','r')
baca = f.read()
f.close()
word = r"di\w+"
diPasif = re.findall(word,baca)
print(diPasif)

#Nomer 3

import re
f=open('Indonesia.txt','r')
baca = f.read()
f.close()
kata = r"di \w+"
diTempat= re.findall(kata,baca)
print(diTempat)


#Nomor 4

f = open('KEI.html', 'r', encoding='latin1')
teks = f.read()
f.close()
i = r'\s<td>[\d\.\w\/]+</td>'
p = r'(\w+)</a></td>' + i + i + i + r'\s<td>([\d\.\w\/]+)</td>'
cocok = re.findall(p, teks)
cocok1 = [(i[0], float(i[1])) for i in cocok]
print(cocok1)
