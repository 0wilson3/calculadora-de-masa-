peso = float(input("escriba su peso en kg:"))
altura = float(input("escriba su estatura en metros:"))
IMC = peso / altura**2
print("su indice de masa corparal es:" + str(round(IMC,2)))

if IMC >=0 and IMC   <=15.99:
    print("delgadez severa")

if IMC >=16 and IMC  <=18.5:
    print ("bajo peso")

if IMC >=18.6 and IMC <=24.9:
    print("normal")

if IMC >=25 and IMC   <=29.9:
    print("sobrepeso") 
 
if IMC >=30 and IMC  <=100:
    print ("obeso")