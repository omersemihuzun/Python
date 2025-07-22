class Meyve():

    def __init__(self,isim,kalori):
        self.isim = isim
        self.kalori = kalori

    def __str__(self):
        return f"{self.isim} şu kadar kaloriye sahiptir: {self.kalori}"

    def __len__(self):
        return self.kalori

muz = Meyve("muz",150)


benimListem = [1,2,3,"a",6]
print(len(benimListem))
print(muz)
print(len(muz))

elma = Meyve("Elma", 200 )
print(elma)
print(len(elma))