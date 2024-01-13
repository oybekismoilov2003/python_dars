def talaba_info(ism,familya,ochestva,t_joyi,yosh):
    talaba={"ism":ism,
            "familya":familya,
            "otasining ismi":ochestva,
            "tugilgan joyi":t_joyi,
            "yosh":yosh}
    return talaba
def talaba_kirituvchi():
    talabalar=[]
    while True:
        familya=input("famiyyangizni kiriting:")
        ism=input("ismingizni kirirting:")
        ochestva=input("Otangizni ismingizni kiriting:")
        t_joyi=input("qayda tug'ilgansz:")
        yosh=input("necha bahorni kordingiz:")
        javob=input("yana talabalar bormu(ha/yo'q'):")
        talabalar.append(talaba_info(ism, familya, ochestva, t_joyi, yosh))
        if javob=="yo'q":
            break
    return talabalar
def info_print(talaba_info):
    print(f"{talaba_info['ism'].title()} {talaba_info['familya'].title()}"
          f" {talaba_info['otasining ismi'].title()} {talaba_info['tugilgan joyi'].title()} da tug'ilgan"
          f" {talaba_info['yosh']} yoshda")
        
    
        