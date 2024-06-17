def menu():
    print ("")
    print ("-_-_-M E N U-_-_-")
    print ("")
    print ("1.- Agregar plan")
    print ("2.- Listar planes")
    print ("3.- Eliminar plan por ID")
    print ("4.- Generar bbdd")
    print ("5.- Cargar bbdd")
    print ("6.- Estadísticas")
    print ("0.- Salir")
    print ("")

def promedio:
        
import csv

lista=[]
promedio=promedio()
EfecAlto=lista
try:
    while True:
        menu()
        op=int(input("Seleccione una opcion: "))
        print ("")
        if op==1:
            print ("-_-_-NUEVO PLAN-_-_-")
            print ("")
            ID=int(input("Ingrese el numero del plan: "))
            print ("")
            NombrePlan=input("Ingrese el nombre del Plan: ")
            print ("")
            Efectividad=int(input("Ingrese la efectividad del plan: "))
            print ("")
            while Efectividad>100 or Efectividad<0:
                print ("La efectividad del plan no puede ser mayor a 100 ni menor a 0")
                print ("")
                Efectividad=int(input("Reingrese la efectividad del plan: "))
                print ("")
            if Efectividad>=0 and Efectividad<=25:
                Categoria=("Chiste")
            elif Efectividad>=26 and Efectividad<=50:
                Categoria=("Anecdota")
            elif Efectividad>=51 and Efectividad<=75:
                Categoria=("Peligro")
            elif Efectividad>=76 and Efectividad<=99:
                Categoria=("Atencion")
            elif Efectividad==100:
                Categoria=("Exclavitud")
            Plan={'ID':ID,'NOMBRE':NombrePlan,'EFECTIVIDAD':Efectividad,'CATEGORIA':Categoria}
            lista.append(Plan)    
        elif op==2:
            print ("-_-_-LISTA PLANES-_-_-")
            print ("")
            for y in lista:
                print (y)
        elif op==3:
            print ("-_-_-ELIMINAR PLAN-_-_-")
            print ("")
            quitar=int(input("Coloque el ID del plan que desea eliminar: "))
            print ("")
            for y in lista:
                if quitar==y:
                    print ("Plan eliminado con exito")
                else:
                    print ("Ese plan no existe")
        elif op==4:
            print ("-_-_-GENERAR BBDD-_-_-")
            with open("planes.csv","w",newline="")as plans:
                escribiendocsv=csv.writer(plans)
                escribiendocsv.writerow('ID','NOMBRE','EFECTIVIDAD','CATEGORIA')
                escribiendocsv.writerows(lista)
        elif op==5:
            print ("-_-_-CARGAR BBDD-_-_-")
            print ("")
        elif op==6:
            print ("-_-_-ESTADISTICAS-_-_-")
            print ("")
            print ("Porcentaje promedio de aceptacion: ", promedio)
            print ("Valor del Porcentaje mas alto: ", EfecAlto)
            
        elif op==0:
            print ("¡Muchas gracias por usarme!")
            break
        else:
            print ("Numero no valido, introduzca un valor correcto.")

except:
    print ("Ocurrio un error")
    
        
       
