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
        
def dataStat(x):

    dataNilai=x
    
    sum=0
    for i in range(len(x)):
        sum=sum+x[i]
    a=sum/len(x)
    print("rata-ratanya : "+ str(a))

    b=max(x)
    print("Nilai Maksimalnya : "+ str(b))

    c=min(x)
    print("Nilai Minimalnya : "+ str(c))
  
print(dataStat(dataNilai))
