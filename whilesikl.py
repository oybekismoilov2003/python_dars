print('Elektron bozoor uchun dastur.')
mahsulotlar={}
n=1
while True:
    savol2=(f'{n}-mahsulotni nomi:')
    nom=input(savol2)
    narh=input(f"{nom.title()}ning narhini kiriting:")
    mahsulotlar[nom]=int(narh)
    javob1=input("Yana maxsulot bormi(ha/yo'q):")
    n+=1
    if javob1=="yo'q":
        break   
print('\n')
buyurtmalar=[]
savol0=("Buyurtmalar:")
summa=0
xaridorlar=int(input('Nechta xaridor mavjud:'))
for k in range(xaridorlar):
    print(f"{k+1}-XARIDOR\n")
    n=1
    print(savol0)
    while True:
        savol1=f"{n}-buyurmani kiriting:"
        buyurtma=input(savol1)
        buyurtmalar.append(buyurtma)
        javob=input("yana buyurtmangiz bormi(ha/yo'q):")
        if javob=='ha':
            n+=1
        else:
            break
        print('\n')
    while buyurtmalar:
        buyurtma=buyurtmalar.pop()
        if buyurtma in mahsulotlar.keys():
            narh=mahsulotlar[buyurtma]
            print(f"{buyurtma.title()}ning narxi-{narh}")
            summa+=int(narh)
        else:
            print(f"Bizda {buyurtma.title()} yo'q edi")
        if len(buyurtmalar)==0:
            print(f"\nJami xaridingiz {summa} so'm bo'ldi"
                  f"\nXaridingiz uchun raxmat")