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
# Operadores ariméticos
# 
#  ---------------------------
#  | Simbolo |    Ejemplo    |
#  ---------------------------
#  |   ()    |  a = 10+(5-4) |  
#  |   **    |  a =  2**2    |
#  |   *     |  a =  2*2     |
#  |   /     |  a =  4/2     |
#  |   //    |  a =  5//2    |
#  |   %     |  a =  7%2     |
#  |   +-    |  a =  2+2+8   |
#  ---------------------------

# ()
a = 7
b = 2
#print(a*(b+b))

# **
#print(a**2)
#print(a**3)

# *
#print(a*2)
#print(a*3)

# /
#print(a/b)

# //
#print(a//b)

# %
#print(a%b)


# +-
#print(a+b+b-a)

# Ejemplo

monto_bruto = 175
tasa_interes = 12
tasa_bonificacion = 5

monto_interes = monto_bruto * tasa_interes / 100
importe_bonificacion = monto_bruto * tasa_bonificacion / 100
monto_neto = (monto_bruto - importe_bonificacion) + monto_interes

print(monto_neto)