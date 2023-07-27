class Hegyek:
    
 def __init__(self,hegy_csucs,hegyseg,magassag):
    self.hegy_csucs=hegy_csucs
    self.hegyseg=hegyseg
    self.magassag=magassag
 
lista=[]
def beolvasas():
     f=open("hegyekMo.txt","r",encoding="UTF-8")
     f.readline()
     for i in f:
        reszek=i.strip().split(";")
        hegy_csucs=reszek[0]
        hegyseg=reszek[1]
        magassag=int(reszek[2])
        objektum=Hegyek(hegy_csucs,hegyseg,magassag)
        lista.append(objektum)


def kiir():
    for i in lista:
        print(i.hegy_csucs,i.magassag)

def F3():
    print(f"3.feladat: Hegycsúcsok száma: {len(lista)} db")

def F4():
    ossz=0
    for i in lista:
        ossz+=i.magassag
    atlag=ossz/len(lista)
    print(f"4.feladat: Hegycsúcsok átlagos magassága: {atlag} m")
       
  

def main():
     beolvasas()
     #kiir()
     F3()
     F4()
    
main()