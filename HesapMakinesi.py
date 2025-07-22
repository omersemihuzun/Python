def hesapla(a,b,islem):
    
    if islem not in "+-*/":
        print("Lütfen belirtilen işlemleri kullanın.")
    if islem == "+":
        return(str(a)+ " + " + str(b) + " = " +str(a+b))

    if islem == "-":
        return(str(a)+ " - " + str(b) + " = " +str(a-b)) 

    if islem == "*":
        return(str(a)+ " * " + str(b) + " = " +str(a*b))

    if islem == "/":
        return(str(a)+ " / " + str(b) + " = " +str(a/b))

while True :
    try:
        a  = int(input("İlk sayıyı giriniz :"))        
        b  = int(input("İkinci sayıyı giriniz :"))    
        islem=input("İşlemi seçiniz: +-*/")   
        sonuc = hesapla(a,b,islem)
        print(sonuc)
    except:
        print("Lütfen sayıları doğru girin. ")
