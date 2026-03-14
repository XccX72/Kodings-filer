#CALC Versjon 0.2 28.08.25 - 
import math
import matplotlib as plt
import pandas as pd

print("Velkommen til CALC 0.2. Hva kan jeg hjelpe deg med?")

antallVar = float(input("Hvor mange variabler bør kalkulatoren bruke? MAKS 2 variabler - "))

versjon = 0.3
resultat = 0
resultat2 = 0

var1 = float(input("Gi en verdi for 1. variabelen din - "))
var1RegOpp = str(input("Skal variabelen være opphøyd, rot eller logaritme, funksjon? ")).lower()
if var1RegOpp == "opphøyd":
    var1Opphoyd = float(input("Hvilken verdi skal tallet være opphøyd i? "))
    resultat = var1**var1Opphoyd

elif var1RegOpp == "rot":
    var1Root = float(input("Hvilken verdi skal roten være? "))
    resultat = var1**(1/var1Root)

elif var1RegOpp == "logaritme":
    var1Log = float(input("Hva er grunntallet i logaritmen? "))
    resultat = math.log(var1, var1Log)




elif var1RegOpp == "funksjon":

    def var1Fun(x):
        return var1 










else:
    print(f"CALC {versjon} forsto ikke hva du skrev. Prøv på nytt!")

#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

ekstraLedd = input("Vil du legge til et ekstra ledd i operasjonen din? (ja/nei) ").lower()

if ekstraLedd == "ja":
    andreRegneOperasjon = input("Hvilke operasjon vil du ha nå? (+, -, *, /, **) ")
    var2 = float(input("Gi en verdi for variabelen din - "))
    var2RegOpp = str(input("Skal 2. variabelen være opphøyd, rot eller logaritme? ")).lower()

    if var2RegOpp == "opphøyd":
        var2Opphoyd = float(input("Hvilken verdi skal tallet være opphøyd i? "))
        resultat2 = var2**var2Opphoyd

    elif var2RegOpp == "rot":
        var2Root = float(input("Hvilken verdi skal roten være? "))
        resultat2 = var2**(1/var2Root)

    elif var2RegOpp == "logaritme":
        var2Log = float(input("Hva er grunntallet i logaritmen? "))
        resultat2 = math.log(var2, var2Log)

    elif var2RegOpp == "nei":
        print("2 Variabel forblir det samme")

    else:
        print(f"CALC {versjon} forsto ikke hva du skrev. Prøv på nytt!")

    if andreRegneOperasjon == "+":
        resultat += resultat2
    elif andreRegneOperasjon == "-": 
        resultat -= resultat2
    elif andreRegneOperasjon == "*":
        resultat *= resultat2
    elif andreRegneOperasjon == "/":
        resultat /= resultat2
    elif andreRegneOperasjon == "**":
        resultat **= resultat2

print(resultat)


