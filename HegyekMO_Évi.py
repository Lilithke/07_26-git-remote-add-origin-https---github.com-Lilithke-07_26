class Hegyek:
    
 def __init__(self,hegy_csucs,hegyseg,magassag):
    self.hegy_csucs=hegy_csucs
    self.hegyseg=hegyseg
    self.magassag=magassag
 def labban(self):
     return self.magassag*3.280839895
 
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

def F5():
    leg=lista[0]
    for i in lista:
        if leg.magassag<i.magassag:
            leg=i
        
        
    print(f"5.feladat: A legmagassabb hegycsúcs adatai:")
    print(f"\tnev:{leg.hegy_csucs}")
    print(f"\thegyseg:{leg.hegyseg}")
    print(f"\tmagassag:{leg.magassag} m")

def F6():
    szam=int(input("6.feladat: Kérek egy magassagot: "))
    
    for i in lista:
        if i.hegyseg=="Börzsöny" and i.magassag > szam:
            print(f"\tVan {szam}m-nél magasabb hegycsúcs a Börzsönyben!")
            break
    else:
            print(f"\tNincs {szam}m-nél magasabb hegycsúcs a Börzsönyben!")

def F7():
    db = 0
    for i in lista:
        if i.labban()>3000:
            db+=1
    print(f"7.feladat: 3000 lábnál magassabb hegycsúcsok száma:{db}")

def F8():
    db1=0
    db2=0
    db3=0
    db4=0
    db5=0
    for i in lista:
        if i.hegyseg=="Mátra":
            db1+=1
            
        elif i.hegyseg=="Bükk-vidék":
            db2+=1
        
        elif i.hegyseg=="Börzsöny":
            db3+=1

        elif i.hegyseg=="Zempléni-hegység":
            db4+=1
        elif i.hegyseg=="Kőszegi-hegység":
            db5+=1
    print(f"8.feladat: Hegység statisztika")
    print(f"\t Mátra - {db1} db")
    print(f"\t Bükk-vidék - {db2} db")
    print(f"\t Börzsöny- {db3} db")
    print(f"\t Zempléni-hegység - {db4} db")
    print(f"\t Kőszegi-hegység - {db5} db")


    


       
  

def main():
     beolvasas()
     kiir()
     F3()
     F4()
     F5()
     F6()
     F7()
     F8()
    
main()