savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
print(savol)
savol1= "Musbat son kiriting "
savol1+= "(dasturni to'xtatish uchun 'exit' deb yozing): "
while True:
    qiymat =input(savol1)
    if str(qiymat.lower())=='exit':
        break
    elif int(qiymat)>=0:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
    else:
        print('manfiy sondan ildiz chiqara olmayman')
print('Dastur tugadi!!!!')
    
    