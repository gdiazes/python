###########################################################################
# Semestre : 2020-1                                                        #
# Curso    : Programación                                                  #
# Sesión   : 0bjetivo :                                                    #
#            - Crear programas usando diferentes tipos de datos            #
#            - Identificar los diferentes tipos de operadores y utilizarlos#
#            para resolver problemas.                                      #                                                                         #
# Autor    :                                                               #
# Versión  :1.0                                                            #
# Fecha de modifcación:                                                    #
############################################################################

# Tipos de datos
# Booleano
# Operador (not)  not true = False
#
#        NOT
#   A  |  OUTPUT |
#  ---------------
#   0  |   1     |  
#   1  |   0     |
#  ---------------

x = True
y = False
#print(not(x))
#print(not(y))


# Operador (or)   1 or 0  = True
#
#        OR
#   A  |  B  | OUTPUT |
#  -------------------
#   0  |  0  |  0     |  
#   0  |  1  |  1     |
#   1  |  1  |  1     |
#   1  |  0  |  1     |
#  -------------------
A = True
B = False
#print(A or B)

# Operador (and)  1 and 1 = True
#
#        AND
#   A  |  B  | OUTPUT |
#  -------------------
#   0  |  0  |  0     |  
#   0  |  1  |  0     |
#   1  |  1  |  1     |
#   1  |  0  |  0     |
#  -------------------
A = False
B = True
print(A and B)
