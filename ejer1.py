num= int(input("ingresa un numero del 1 al 7: "))
dias_semana={
                 1:"lunes",
                 2:"martes",
                 3:"miercoles",
                 4:"jueves",
                 5:"viernes",
                 6:"sabado",
                 7:"domingo"
         }
if num in dias_semana:
        print ("el dia correspondiente es: ", dias_semana[num])
else:
        print("el numero no se encuentra  en el rango")