#test.py>
from string_utils import *

def string_separation_test():
	# Valida el indice de donde se debe cortar el texto
	# esta es una frase larga
	indice_break = string_separation("esta es una frase larga")
	assert indice_break == 12, "Should be 12 but is "+str(indice_break)

if __name__ == "__main__":
    string_separation_test()
    print("Everything passed")
