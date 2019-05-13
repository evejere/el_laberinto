# creamos un archivo nuevo
# guardamos en la carpeta del repositoripo con la extension .py
# uso de numeros aleatorios 


from random import randint   # importamos la libreria randint
aleatorio= randint(0, 20)   # creamos una variable y generamos un numero
#aleatorio entre 0 y 20
print(aleatorio)  #  imprimimos el numero generado


#ejercicio
#escribir una funcion sorteo() que reciba una lista de participantes
#y elegir a uno de los participantes aleatoriamente, y retornar 
#a esa persona elegida
#desasfio: no volver a retornar una persona ya sorteada


from random import randint# importamos  la funcion front import de la libreria

def personas(participan):#definimos una funcion
    #utilizamos len para saber la cantidad de personas que hay en la lista y guardamos en cant
    participantes= len(participan)-1#se le resta 1 porque la lista empieza en 0
    indice=randint (0,participantes)# creamos una variable y generamos un numero aleatorio
    ganador=participan[indice]
    #seleccionamos un participante de la lista para 
    # guardarlo en la variable
    return ganador #retornamos ganador
participantes=["jose","carlos","brahian","matias"] # lista
ganar= personas(participan)#llamamos a la funcion y guardamos en la variable
#el resultado retornado por la funcion
print(ganar)#imprimimos el ganador
 








