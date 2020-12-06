myData=[]
print("Berapa kali perulangan? = ",end="")
n=int(input())
while True:
    if n==0:
        break
    else :
        print("Masukan bilangan bulat : ",end="")
        nilai=str(input())
        myData=myData+[nilai]
        n=n-1

def sortStringByChar(myData):
    print("myData : ",myData)
    myData.sort(reverse=True)
    print("myData : ",myData)

sortStringByChar(myData)
