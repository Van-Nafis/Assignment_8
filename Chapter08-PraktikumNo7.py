hargaBuah={5000:"apel",8500:"jeruk",7800:"mangga",6500:"duku"}
def hargaMahal(hargaBuah):
    data=list(hargaBuah.keys())
    data.sort(reverse=True)
    for x in data:
        print(x)
    

hargaMahal(hargaBuah)
