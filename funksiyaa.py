#def yosh_xisobla(ism,yosh):
#    """Ismii sorab yosh xisoblovchi funksiya"""
#   print(f"Salom {ism.title()},sizning yoshingiz {2023-yosh} da")
#ism=input("Ismingiz:")
#yosh=int(input(f"{ism.title()} nechanchi yil tug'ilgansz:"))
#yosh_xisobla(ism, yosh)
#def kvadrat_kub_xisobla(son):
#   """Son sorab olib uning kv va kubini xisoblovchi funksiya"""
#    print(f"{son} ning kvadrati {son**2},kubi esa {son**3}")
#son=int(input("son kiriting:"))
#kvadrat_kub_xisobla(son)
#def juft_toq_tekshir(son):
#   """sonni olib juft yoki toqlikka tekshiruvchi funksiya"""
#    if son%2==0:
#       toq_juft="juft"
#   else:
#        toq_juft="toq"
#    print(f"{son} -{toq_juft} ekan")
#son=int(input("sonni kiriting:"))
#juft_toq_tekshir(son)
#def taqqosla(son1,son2):
#    """ikkita sonni olib ularni taqqoslovchi funksiya"""
#    if son1>son2:
#        son=son1
#    elif son2>son1:
#        son=son2
#       print(f"bu ikki sondan kattasi {son}")
#    if son1==son2:
#        print("sonlar teng")
#son1=int(input("birinchi son:"))
#son2=int(input("ikkinchi son:"))
#taqqosla(son1, son2)
def boluvchilarini_top(son):
    """foydalanuvchidan son olib uni 10 gacha bo'luvchilarini topuvchi funksiya"""
    for n in range(2,11):
        if son%n==0:
            print(f"{son} {n} ga bo'linadi")
son=int(input("sonni kiriting:"))
boluvchilarini_top(son)