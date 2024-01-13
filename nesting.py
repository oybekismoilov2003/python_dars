davlatlar={'ispaniya':{
    'poytaxti':'madrid',
    'mashxur klub':'real madrid',
    'mashxurligi':'futbol'},
    'rossiya':{
        'poytaxti':'maskva',
        'mashxur klub':'sska',
        'mashxurligi':"o'rmon"},
    "o'zbekiston":{
        'poytaxti':'toshkent',
        'mashxur klub':'paxtakor',
        'mashxurligi':'qora ishchi yetkazish'}}
chiroq=input("qaysi davlat haqida malumot kerak:")
for davlat,malumotlar in davlatlar.items():
    if davlat==chiroq.lower():
        print(f"{davlat.title()}:")
        for malumot,malum in malumotlar.items():
            print(f"{malumot}-{malum.title()}")