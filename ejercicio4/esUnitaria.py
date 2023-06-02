import sys
sys.path.append("..")

from ejercicio3 import esEscalar as fu

def esUnitaria(m):
    return m[0][0] == 1 and fu.esEscalar(m)
