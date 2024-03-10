import sys
sys.path.append('../')
import pantalla
import time
from datetime import datetime
import actuator
import pprint
from flask import *

app = Flask(__name__)
my_pantalla = pantalla.Pantalla()
actuator = actuator.Actuator(25,24,23)

#TODO: Check if there are some previous settings

@app.route("/", methods=["GET","POST"])

def home():
	if request.method == "POST":
		color_hex = request.form["color"]
		#HEX to RGB
		color_rgb = tuple(int(color_hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
		my_pantalla.setColor(color_rgb[0], color_rgb[1], color_rgb[2])
		
		# Modo reloj
		if request.form['submit_button'] == 'Clock Mode':
			while True:
				current_time = datetime.now()
				my_pantalla.showSectionedMessage(current_time.strftime("%H:%M:%S"),"")
				time.sleep(1)
		
		# Mover al mono
		if request.form['submit_button'] == 'Up':
			actuator.extend()
		if request.form['submit_button'] == 'Down':
			actuator.retract()
		
		message1 = request.form["message1"]
		message2 = request.form["message2"]
		
		# Sanitize double spaces
		if message1:
			" ".join(message1.split())
		
		if message2:
			" ".join(message2.split())
		
		my_pantalla.showSectionedMessage(message1, message2)
	
	return render_template("home.html")
	
if __name__ == "__main__":
    app.run(debug=True,host='192.168.86.192')
