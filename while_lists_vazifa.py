buyurtmalar=[]
while True:
    buyurtma=input('nima buyurtma qilasiz:')
    buyurtmalar.append(buyurtma)
    print('Buyurtmanggiz qabul qilndi')
    savol=input('yana biror narsa buyurtma qilaszmi?:')
    if savol!='ha':
        break



mahsulotlar={}
while True :
    mahsulot=input('mahsulot nomini kiriting:')
    narx=input('mahsulot narxii kiriting:')
    mahsulotlar[mahsulot]=narx
    javob=input('yana mahsulot qowaszmi(ha\yoq):')
    if javob!='ha' or javob=='yoq':
        break


while buyurtmalar:
    buyurtma=buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narx=mahsulotlar[buyurtma]
        print(f"{buyurtma.title()}-{narx} som")
    else:
        print('bizda bunday mahsulot yoq afsusdamz')

















