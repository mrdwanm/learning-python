def jumlah (*tup_angka):
    hasil = 0
    for angka in tup_angka:
        hasil += angka
    return hasil
# return mengembalikan hasil dan dapat menyimpan ke dalam variable
# *tup_angka / *args digunakan untuk parameter (tupple) lebih fleksibel
# ** kwargs digunakan untuk parameter dictionary/tupple lebih fleksibel
a = 6
b = 1
c = 2
jumlah = jumlah(a,b,c)
print(f"hasil dari {a} + {b} = {jumlah}")

