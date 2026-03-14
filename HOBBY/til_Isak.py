import matplotlib.pyplot as plt
import pandas as pd
import math


# hei danni, my boy, isak her
# dette er det jeg har gjort:
# 1. lagt til en variabel for versjonsnummer slik at du slipper å oppdatere meldingen hvor det står "calc (versjon) forsto ikke..."
# 2. fjernet mellomrom mellom 'print' og parantesen - det ser bedre ut
# 3. lagt til ekstra output når regnestykket er ferdig; 'x opphøyd i x er x', osv.
# 4. lagt til en input som spør brukeren om han vil legge til et ekstra ledd til operasjonen sin, som du ville gjøre
# 5. lagt til funksonalitet for et annet ledd i koden
#    hvis brukeren vil ha et annet ledd, så spør den hvilke operasjon han vil bruke (+, -, osv) og hvilke annet tall han vil ha
#    etter dette er det ganske selvforklarende.
# 6. lagt til en variabel som heter resultat
#    det er bedre å ha bruke en variabel for å lagre resultatet, fordi da setter du bare verdien av variabelen i første delen av koden, og så printer du den ut på
#    slutten. hvis brukeren har lyst til å legge til et annet ledd, kan programmet nå se hva resultatet fra det første leddet var ved å se på variabelen. :D


var1 = 5

AntLedFun = int(input("Hvor mange ledd skal funksjonen ha?"))

if AntLedFun == 1:
    FunLed1 = float(input("Hva skal ledd verdi være? "))
    ResFun1 = FunLed1

elif AntLedFun == 2:
    FunLed1 = float(input("Hva skal første ledd verdu være - "))
    FunLed2 = float(input("Hva skal andre ledd verdu være - "))
    andreRegneOperasjon2 = input("Hvilke operasjon vil du ha nå? (+, -, *, /, **) ")


elif AntLedFun == 3:
    FunLed1 = float(input("Hva skal første ledd verdu være - "))
    andreRegneOperasjon3 = input("Hvilke operasjon vil du ha nå? (+, -, *, /, **) ")
    FunLed2 = float(input("Hva skal andre ledd verdu være - "))
    andreRegneOperasjon4 = input("Hvilke operasjon vil du ha nå? (+, -, *, /, **) ")
    FunLed3 = float(input("Hva skal tredje ledd verdu være - "))


def var1Fun(x):
        return ResFun1

print(ResFun1)