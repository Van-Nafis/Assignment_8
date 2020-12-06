namaMhs=[]
i=1
while True:
    print("Masukan Nama Mhs. ke-"+str(i)+" : ",end="")
    x=str(input())
    namaMhs=namaMhs+ [x]
    print("Masukan Lagi? (y/n) : ")
    tanya=str(input())
    if tanya=="n":
        break
        
    elif tanya=="y":
        
        i=i+1
        
    else:
        print("perintah salah, masukan lagi")

for nilai in range(len(namaMhs)):
    namaMhs.sort()
    print(namaMhs[nilai],end=" ")
    print("(",(len(namaMhs[nilai]))," karakter)")
