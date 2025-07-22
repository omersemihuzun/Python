def hesapla(a,b,islem):

    if islem == "+":
        return (str(a)+ " + " + str(b) + " = " +str(a+b))

    if islem == "-":
        return (str(a)+ " - " + str(b) + " = " +str(a-b)) 

    if islem == "*":
        return (str(a)+ " * " + str(b) + " = " +str(a*b))

    if islem == "/":
        return (str(a)+ " / " + str(b) + " = " +str(a/b))


a  = int(input("İlk sayıyı giriniz :"))        
b  = int(input("İkinci sayıyı giriniz :"))    
islem = int(input("İşlemi seçiniz : +-*/"))    
hesapla(a,b,islem)