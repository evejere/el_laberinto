#juego de adivinar el numero, todos juntos,
#adivinar un numero generado aleatoriamente,
#ir introduciendo por teclado el numero a adivinar


from random import randint
generado=randint(0,10)
#print(generado)       trampa
condicion=True
while condicion:
    numero=input("dame un numero del 0 al 10: ")
    if generado==int(numero):#comparamos el numero introducido 
        print("ganaste una amvorgesa que Lore paga")
        condicion=False
    else:
        print("el perdedor compra pizza a lore")



from random import randint
generado=randint(0,10)
#print(generado)       trampa
condicion=True
intento=10
while condicion:
    if intento>0:
         numero=input("dame un numero del 0 al 10: ")
         intento=intento-1
         if generado== int (numero):
             print("ganaste una amvorgesa que Lore paga")
             condicion=False
        else:
            print("el perdedor compra pizza a lore")
            print("te quedan", intento,"intentos")
    else:
        condicion=False
        print ("perdiste")