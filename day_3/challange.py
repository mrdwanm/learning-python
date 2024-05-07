tambah = "y"
pesanan =[]
while tambah !="n":
    if tambah == "y":
        pesan = input("masukkan pesanan anda:")
        pesanan.append(pesan)
    else:
        print("perintah tidak sesuai")
    tambah = input("apakah anda ingin pesan lagi? (y/n)")
    tambah = tambah.lower()
jumlah = len(pesanan)
print(f"jumlah pesanan anda {jumlah} item")
for i in pesanan:
    print(f"anda telah memesan: {i}")