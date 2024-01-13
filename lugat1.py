menu={'somsa':8000,
      "osh":23000,
      "shorva":18000,
      "manti":"donasi 6000",
      "shashlik":"six 14000",
      "xonim":5000,
      "chuchvara":22000,
      "choy":3000,
      'salat':4000,
      'non':3500}
buyurtma=[]
print("3 ta maxsulot buyurtma bering:")
for n in range(3):
    buyur=input(f"{n+1}-buyurtma:")
    buyurtma.append(buyur.lower())
for ovqat in buyurtma:
    if  ovqat in menu:
        print(f"{ovqat.title()} {menu[ovqat]} so'm.")
    else:
        print(f"bizda {ovqat.title()} yo'q")
    
    
    
    
    