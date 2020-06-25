class Kitaplar():
    def __init__(self,isim,yazar,sayfa,tür):
        print("init fonksiyonu")
        self.isim = isim
        self.yazar = yazar
        self.sayfa = sayfa
        self.tür = tür

    def __str__(self):
        return "isim {}\n Yazar: {}\n Sayfa: {}\n Tür:{}".format(self.isim,self.yazar,self.sayfa,self.tür)

    def __len__(self):
        return self.sayfa

    """def __del__(self):
        print("Kitap objesi siliniyor.........")"""



kitap = Kitaplar("İstanbul Hatirası","Ahmet Candan",234,"korku")
print(kitap)
print(len(kitap))
#del kitap
print(kitap)