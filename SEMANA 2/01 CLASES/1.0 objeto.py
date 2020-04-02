###########################################################################
# Semestre : 2020-1                                                        #
# Curso    : Programación                                                  #
# Sesión   : 0bjetivo :                                                    #                                                                         #
# Autor    :                                                               #
# Versión  :1.0                                                            #
# Fecha de modifcación:                                                    #
# mismo nombre pero con diferente valor.                                   #                                                  #
############################################################################


#Sintaxis para definir una clase
# class   NOMBREDELACLASE:
class Coche:              #al finalizar utilizamos los :
    numero_de_ruedas = 4  #definimos un atributo con un valor.

    def desplazamiento(self): #ahora podemos defini (def) un comportamiento (método)
                          #para diferenciar un método de una función usamos la palabra reservada (self)
        #pass                  #la palabra reservada (pass), le indicará al interprete de python que no se a definido ningún funcionamiento
        print("El coche se esta desplazando sobre 4 ruedas") #El comportamiento definido es mostrar un mensaje

class Moto():
    ruedas=2
    def desplazamiento(self):
        print("La moto se esta desplazando sobre 2 ruedas")


miVehiculo = Coche()          #Definimos un objeto y especificamos a que clase pertenece

print("Mi coche tiene ", miVehiculo.numero_de_ruedas, " ruedas") #Para mostrar un atributo podemos usar la siguiente sintaxis: miObjeto.atributo

miVehiculo.desplazamiento()  #Para referenciar a un método, usaremos la siguiente sintaxis: miObjeto.metodo()

print("---------------Segundo objeto---------------")
miVehiculo2=Moto()
print("Mi moto tiene ", miVehiculo2.ruedas, " ruedas")
miVehiculo2.desplazamiento()
    
    