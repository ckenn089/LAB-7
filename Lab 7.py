import machine
import time
line = 0
servo_pin = 14  
gcode_list = []
 
#Initilizes variables for pico, and list storing the gcode values
servo = machine.PWM(machine.Pin(servo_pin), freq=50)  # Create a PWM object for the servo


#Function that translates the coorosponding angle to the input
def translate(angle: float) -> int:


	MIN = 1638 # 0 degrees
	MAX = 8192 # 180 degrees
	DEG = (MAX - MIN) / 180 # value per degree

	# clamp angle to be between 0 and 180
	angle = max(0, min(180, angle))

	return int(angle * DEG + MIN)


#Takes the file of the shape you want, opens and reads it, and appends those values into a list while striping the white space
def read_file (line):

	with open("line.gcode", "r") as f:
		for line in f:
			gcode_list.append(line.strip())
			print (gcode_list)

	return line
#Would take the hytpothetical commands, reads them and pulls the appropriate gcode from the list, and translates that into angles.
def command_interpreter():


	return None
#Simply sends the translate function to be stored on the pico
def send_to_pico():
	servo.duty_u16(translate(90))
	return None
command_interpreter()
read_file(line)
send_to_pico()
translate(90)