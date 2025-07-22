
class Hayvan():
        def __init__(self):
            print("hayvan sınıfı init çağrıldı ")
    
        def method1(self):
            print("hayvan sınıfı method 1 ")

        def method2(self):
            print("hayvan sınıfı method 2 ")


benimHayvanim= Hayvan()
benimHayvanim.method1()
benimHayvanim.method2()

class Kedi(Hayvan):
    def __init__(self):
        Hayvan.__init__(self)
        print("Kedi init çağrıldı")

    def miyavla(self):
        print("miyav!")
    ##override 
    def method1(self):
        print("kedi sınıdınfan method 1 ")

benimKedi=Kedi()
benimKedi.method1()
benimKedi.miyavla()

digerKedi = Kedi()
digerKedi.method1()
 