mahsulotlar=[]  
print("online shopda mavjud bo\'lgan mahsulotlarni kirituvchi  dastur")            #this code is for adminss of service.admins should enter products what are in shop
while True:                                          
    mahsulot=input('Qanday mahsulot kiritasiz?:') 
    mahsulotlar.append(mahsulot)
    print('mahsulot  ro\'yxatga kiritildi')
    savol=input('yana biror mahsulot kiritasizmi ?:(ha,yo\'q')
    if savol!='ha':
        break



buyurtmalar={}  
print("buyurtma qabul qiluvchu dastur")                            #this code is for users.they should enter meal which the want to buy.the are able to buy more than once
while True :
    buyurtma=input(' Buyurtmma qilmoqchi bolgan mahsulot nomini kiriting:')
    narx=input('Mahsulot narxini kiriting:')
    buyurtmalar[buyurtma]=narx
    javob=input('Yana mahsulot qoshasizmi(ha\yo\'q):')
    if javob!='ha':
        break


while mahsulotlar:
    mahsulot=mahsulotlar.pop()
    if mahsulot  in buyurtmalar.keys():
        narx=buyurtmalar[mahsulot]
        print(f"{mahsulot.title()}-{narx} som")
    else:
        print('Bizda bunday mahsulot yoq afsusdamz')














