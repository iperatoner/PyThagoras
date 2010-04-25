#!/usr/bin/env python3.1

werte = ['a', 'b', 'c', 'h', 'p', 'q', 'A', 'alpha', 'beta'] #Zuweisung der möglichen punkte

def main():
    if False:
        pass #Der Text für die Parameterabfrage
        
    else:
        geg = [] #die gegebenen punkte
        wertgeg = [] #die werte der gegebenen punkte
        eingabe = input("Was ist gegeben? (Trennung erfolgt durch Kommata): ")
        letter = eingabe.split(',') #
        for char in letter:
            if char in werte:
                geg.append(char) #bekannte punkte rausfiltern und zu den gegebenen hinzufügen
                
        for el in geg:
            wertgeg += (input("Wert von %s: " %(el)))

        beka = dict(zip(geg,wertgeg)) #bekannte punkte sind nun in einem dictionary mit den werten

        
        
if __name__ == '__main__':
    main()
