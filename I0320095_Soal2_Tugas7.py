nilai_mahasiswa = input("Masukkan nilai (dipisahkan dengan spasi) : ").split()

#Konversi menjadi tipe int
for i in range(len(nilai_mahasiswa)):
    nilai_mahasiswa[i] = int(nilai_mahasiswa[i])

#Mencari rata-rata nilai
mean = sum(nilai_mahasiswa)/len(nilai_mahasiswa)

print("Nilai yang diinput : ", nilai_mahasiswa)
print('-'*50)

import math
print("Nilai Tertinggi = ", max(nilai_mahasiswa))

print("Nilai Terendah = ", min(nilai_mahasiswa))

print("Rata-rata nilai = ", mean)

print("Rata-rata nilai (pembulatan ke atas) =".upper() , math.ceil(mean))

print("Rata-rata nilai (dengan pembulatan ke bawah) =".upper() , math.floor(mean))