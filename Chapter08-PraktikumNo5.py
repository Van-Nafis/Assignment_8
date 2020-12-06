dataNilai=[]
print("Berapa kali perulangan? = ",end="")
n=int(input())
while True:
    if n==0:
        break
    else :
        print("Masukan bilangan bulat : ",end="")
        nilai=int(input())
        dataNilai=dataNilai+[nilai]
        n=n-1

def kuadrat(dataNilai):
    print("Bilangan yang akan dipangkat : ",dataNilai[0:])
    print("Hasil pangkatnya : [ ",end="")
    for tiap in range(len(dataNilai)):
        dataBaru=dataNilai[tiap]**2
        print(dataBaru,end=" ")
    print("]")
kuadrat(dataNilai)
