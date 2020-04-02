###########################################################################
# Semestre : 2020-1                                                        #
# Curso    : Programación                                                  #
# Sesión   : 0bjetivo :                                                    #                                                                         #
# Autor    :                                                               #
# Versión  :1.0                                                            #
# Fecha de modifcación:                                                    #
# Polimorfismo: El polimorfismo en python es la capacidad que tienen los   #
# objetos de diferentes clases para usar un comportamiento o atributo del  #
# mismo nombre pero con diferente valor.                                   #                                                  #
############################################################################

class Coche():
    ruedas=4
    def desplazamiento(self):
        print("El coche se esta desplazando sobre 4 ruedas")
class Moto():
    ruedas=2
    def desplazamiento(self):
        print("La moto se esta desplazando sobre 2 ruedas")