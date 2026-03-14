#Basic Calculator, Dato. 6-12-24 - Nåtid
import math

print("Alle input skal skrives med stor bokstav foran")

x=float(input("Skriv en verdi for X = "))
y=float(input("skriv en verdi for y = "))

#X BIT

p_sq_x_1=(input("vil du ha x verdi OPPHØYD eller KVADRATROT? Kvadratrot/Opphøyd/Nei = "))

#Bare hvis DE SKAL ha opphøyd eller kvadrarot
if p_sq_x_1=="Kvadratrot":
    verdi_p_sq_x_1=input("Hvor masse skal Kvadratroten være? (Akkurat nå fungere ikke denne funksjonen) = ")
    x=(math.sqrt(float(x)))  #prøv å adde sånn at vi kan opphøye den
elif p_sq_x_1=="Opphøyd":
    verdi_p_sq_x_2=int(input("Hvor masse skal Oppøhyd være? = "))
    x=x**verdi_p_sq_x_2
elif p_sq_x_1=="Nei":
    print("X for ikke Kvadratrot eller Opphøyding")

#Y BIT

p_sq_y_1=(input("vil du ha y verdi OPPHØYD eller KVADRATROT? Kvadratrot/Opphøyd/Nei = "))

#Bare hvis DE SKAL ha opphøyd eller kvadrarot
if p_sq_y_1=="Kvadratrot":
    verdi_p_sq_y_1=input("Hvor masse skal Kvadratroten være? = ")
    y=(math.sqrt(float(y)))  #prøv å adde sånn at vi kan opphøye den
elif p_sq_y_1=="Opphøyd":
    verdi_p_sq_y_2=int(input("Hvor masse skal Oppøhyd være? = "))
    y=y**verdi_p_sq_y_2
elif p_sq_x_1=="Nei":
    print("Y for ikke Kvadratrot eller Opphøyding")

#PLUSS, MINUS, GANGING og DELING bit

v_ganging=(x*y)
v_ingen=(x, y)


Variabel_a=input("Vil du ta , Ganging, Deling, Pluss, Minus eller Ingen av de? Svar her = ")

if Variabel_a=="Ganging":
    print(v_ganging)

elif Variabel_a=="Deling":
    V_deling=input("x/y eller y/x = ")
    if V_deling=="x/y":
        print(x/y)
    elif V_deling=="y/x":
        print(y/x)

elif Variabel_a=="Pluss":
    print(x+y)

elif Variabel_a=="Minus":
    V_minus=input("x-y eller y-x")
    if V_minus=="x-y":
        print(x-y)
    elif V_minus=="y-x":
        print(y-x)

elif Variabel_a=="Ingen":
    print(v_ingen)

else:
    print("Du bruker ikke kalkulatoren")


