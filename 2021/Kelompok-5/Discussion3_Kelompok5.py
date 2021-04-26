import hashlib
import re

print('='*36)
print('Kelompok E')
print('Oleh : \nKadek Vincky Sedana\t1808561071\nI Kadek Aldy Oka Ardita\t1808561091\n')
print('Tugas Kriptoanalis')
print('='*36)

word = input('Masukkan Kalimat : ')
ubah = re.compile("[^a-zA-Z]")
word = ubah.sub("", word)

my_data = []
db_hash = []

for i in range(len(word)):
    for j in range(len(word)):
        my_data.append(word[i] + word[j])

for i in range(len(my_data)):
    hash_result = hashlib.sha256(str(my_data[i]).encode())
    result = hash_result.hexdigest()
    print("Hasil SHA256 dari: ")
    print(my_data[i])
    print("adalah")
    print(result)
    db_hash.append(my_data[i] + "---" + result)

file = input("Masukkan Nama File : ")
report = open(file+'.txt', 'w')
for element in db_hash:
    report.write(element)
    report.write('\n')
report.close()
