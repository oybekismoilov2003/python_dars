ismlar=['ali','vali','soli']
def bahola(ismlar):
    baholar={}
    for ism in ismlar:
        baho=int(input(f"{ism.title()}-ning bahosi:"))
        baholar[ism]=baho
    return baholar
print(bahola(ismlar))
print(ismlar)
        