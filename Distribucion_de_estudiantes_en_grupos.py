
import random
##########################################

lgrupos=[]
lnombres=[]   #listas
ltemas=[]

#########################################

path1, path2, path3 = input("Introduzca el directorio de grupos, nombres y temas: ").split()  #//asigna el string de cada ruta a una variable diferente
grupos = open(path1,"r");
nombres = open(path2,"r");      # abre el documento con el paramentro de lectura "r" read
temas = open(path3,"r");

#########################################

for x in grupos: 
 lgrupos.append(x)
 pass

for x in nombres:                          #for each para guardar cada linea del documento en una lista
 lnombres.append(x)
 pass

for x in temas: 
 ltemas.append(x)
 pass

#########################################

integrantes1 = int(len(lnombres)/len(lgrupos))
integrantes2 = integrantes1+1                                                                #algoritmo para determinar el numero de grupos y de integrantes
sector2 = int(len(lnombres)-(len(lgrupos)*integrantes1))
sector1 = int((len(lnombres)-(sector2*integrantes2))/integrantes1)

###########################################

temas1 = int(len(ltemas)/len(lgrupos))
temas2 = temas1+1
grupos2 = int(len(ltemas)-(len(lgrupos)*temas1))
grupos1 = int(len(ltemas)-((grupos2*temas2)/temas1))

###########################################
for i in range(sector1):
     showgrupo = random.choice(lgrupos)             #muestra un grupo aleatorio
     print (str(showgrupo).strip(), end=" ")
     print ("(Estudiantes: " + str(integrantes1) + ", Temas: "+ str(temas1)+")")
     lgrupos.remove(showgrupo)                      #lo elimina de la lista para que no se repita en la siguiente iteracion
     for i in range(integrantes1):
         showintegrante = random.choice(lnombres)
         print ("{}.".format(i+1) + str(showintegrante).strip(), end=", ")      #la misma logica con los nombres 
         lnombres.remove(showintegrante)
         pass 
     print ("")
     showtema = random.choice(ltemas)
     print ("Temas: " + showtema)
     ltemas.remove(showtema)
     print ("")
     pass
###########################################


for i in range(sector2):
    showgrupo = random.choice(lgrupos)
    print (str(showgrupo).strip(), end=" ")                                         #este es el mismo programa que el anterior solo que este tiene cantidades de grupos con diferente numero de integrantes
    print ("(Estudiantes: " + str(integrantes2) + ", Temas: "+ str(temas2)+")")
    lgrupos.remove(showgrupo) 
    for i in range(integrantes2):
         showintegrante = random.choice(lnombres)
         print ("{}.".format(i+1) + str(showintegrante).strip(), end=", ")
         lnombres.remove(showintegrante)
         pass
    print ("")
    showtema = random.choice(ltemas)
    print ("Temas: " + showtema)
    ltemas.remove(showtema)
    print ("")
    pass
########################################