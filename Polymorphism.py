class Elma():
    def __init__(self,isim):
        self.isim = isim

    def bilgiVer(self):
        return self.isim + " 150 kaloridir. "


class Muz():
    def __init__(self,isim):
        self.isim = isim

    def bilgiVer(self):
        return self.isim + " 100 kaloridir.  "

elma = Elma("elma")
elma.bilgiVer()

muz = Muz("muz")
muz.bilgiVer()

meyveListesi = [elma,muz]

for meyve in meyveListesi:
    print(meyve.bilgiVer())