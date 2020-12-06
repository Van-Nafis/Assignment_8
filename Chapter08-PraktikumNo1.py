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

dataNilai.sort(reverse=True)
print(dataNilai)
