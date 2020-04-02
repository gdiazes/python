###########################################################################
# Semestre : 2020-1                                                        #
# Curso    : Programación                                                  #
# Sesión   : 0bjetivo :                                                    #                                                                         #
# Autor    :                                                               #
# Versión  :1.0                                                            #
# Fecha de modifcación:                                                    #
# La encapsulación es una forma de darle uso exclusivo a los               #
# comportamientos o atributos que posee una clase, es decir, protege esos  #
# atributos y comportamientos para que no sean usados de manera externa.   #
############################################################################

class Ejemplo():
    
    def __init__(self):
        self.__oculto="Me encuentro oculto en la clase"
    def publico(self):
        print("Soy un método público, a la vista de todo")
       
    def __privado(self):                 #Para hacer que un atributo sea privado se usa dos guienes bajos antes del nombre (__)
        print ("Soy un metodo privado, para ti no existo")
    
    def get_oculto(self):
        return self.__oculto
    
    def set_oculto(self):
        self.__oculto = self.__privado()
        
objeto = Ejemplo()                          #Creamos el objeo y referenciamos a la clase
objeto.publico()                     #Imprimimos la información del método publico
objeto._Ejemplo__privado()           #Para mostrar la información tenemos que usar la sintaxi:  _Clase__metodo()
print(objeto.get_oculto())                  #
objeto.set_oculto()                         #