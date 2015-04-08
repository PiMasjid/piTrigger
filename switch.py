from time import sleep
import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

record = 0
buttonPressed = 0
x = 1;
while x > 0:
	#get input from pin 18
	input_state = GPIO.input(18)
	#if button is being press
	if input_state == False:
		buttonPressed += 1
	else:
		#if recording not started yet
		if record == 0:
			if buttonPressed > 0:
				#first press, grab youtube url and run the streaming
				proc = subprocess.Popen("php /home/pi/Desktop/callyoutube.php", shell=True, stdout=subprocess.PIPE)
				response = proc.stdout.read()
	
				#check if response is valid
				#start the camera and stream!
		
				print('Start Recording')
				record = 1
				buttonPressed = 0
		else:
			#if recording has started and button being press more than 3 seconds. Stop recording
			if buttonPressed > 3:
				print('Stop Recording')
				record = 0
				buttonPressed = 0
	sleep(1) #sleep for 1 second