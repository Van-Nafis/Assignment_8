dataSayur=["bayam","kangkung","wortel","selada"]
try:
    while True:
        print("Menu:")
        print("A. Tambah data sayur")
        print("B. Hapus data sayur")
        print("C. Tampilkan data sayur")
        print()
        print("Pilihan Anda: ",end="")
        s=str(input())
        if s=="A":
            print("Masukan data yang akan ditambah : ")
            A=str(input())
            dataSayur.append(A)
        elif s=="B":
            print("Masukan data yang akan dihapus: ")
            B=str(input())
            dataSayur.remove(B)
        elif s=="C":
            print(dataSayur[0:])
        else :
            print("Input tidak valid")
except ValueError:
    print("Data tidak ditemukan")
