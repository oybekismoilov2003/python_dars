def talaba_malumot_chiqar(ism,familiya,**qoshimchalar):
    qoshimchalar['ism']=ism
    qoshimchalar['familiya']=familiya
    return qoshimchalar
ism1=talaba_malumot_chiqar('Oybek', 'Ismoilov', yoshi=21,univer='tuit')
ism2=talaba_malumot_chiqar('alisher', 'abdurasulov',qiziqish='sarguzasht')
print(ism1)