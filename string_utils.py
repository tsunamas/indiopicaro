# string_utils.py>
screen_length = 16

# Esta funcion toma el string
def string_separation(message):
	print("Mensaje: "+message)
	print("char16: "+message[16])
	# si el mensaje 
	if len(message) > screen_length and message[16] == " ":
		#todo ir para atras para pillar el ultimo espacio
		return 16
	else:
		print("no hay espacio")
	return len(message)
