son=int(input("biron son kiriting:"))
qoldiqsiz_bolinadigan_sonlar=[]
for n in range(8):
    if son%(n+2)==0:
        qoldiqsiz_bolinadigan_sonlar.append(n+2)
print(qoldiqsiz_bolinadigan_sonlar)
        
        
        