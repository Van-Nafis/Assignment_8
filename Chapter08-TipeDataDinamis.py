#No.1
a=[1,5,6,3,6,9,11,20]
b=[7,4,5,6,7,1,12,5,9]
#No.2
a.insert(3,10)
b.insert(2,15)
#No.3
a.append(4)
b.append(8)
#No.4
a.sort()
b.sort()
#No.5
c=a[:7]
d=b[2:9]
#No.6
e=[]
for nilai1 in range(len(c)):
    for nilai2 in range(len(d)):
        e=[c[nilai1]+d[nilai2]]

print(a)
print(b)
print(c)
print(d)
print(e)
