abeceda = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Assuming this is defined somewhere
def dekoduj(sifrovany, odposlechnuty):
    abeceda=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    sifrovany=[*sifrovany]
    odposlechnuty=[*odposlechnuty]
    #ERRORY
    if sifrovany not in abeceda or odposlechnuty not in abeceda:
        pass
        #return print("Error: Chybny vstup!")
    if len(odposlechnuty)!=len(sifrovany):
        pass
        #return print("Error: Chybna delka vstupu!")
    
    counter2=0
    reseni=[]
    #VSECHNY POSUNY
    for i in range(len(abeceda)):
        kopie=[]
        counter1=0
        #SLOZ KOPII
        for pismeno in sifrovany:
            a=abeceda.index(pismeno)
            b=(a+i)%len(abeceda)
            kopie.append(abeceda[b])
        c=-1
        #OHODNOT KOPII
        for pismeno_kopie in kopie:
            print(pismeno_kopie, end="")
            c+=1
            if pismeno_kopie==odposlechnuty[c]:
                counter1=counter1+1
        #NAJDI RESENI
        if counter1>counter2:
            reseni=kopie
            print(reseni, end="")
            print(counter1)
        counter2=counter1
    return print(reseni, end="")


dekoduj("xUbbemehbT", "XYlloworld")
print(abeceda[0])


            

        
    

   

