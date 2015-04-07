import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

i = 0
x = 1;
while x > 0:
    input_state = GPIO.input(18)
	if i == 0:
		if input_state == False:
			
			#first press, grab youtube url and run the streaming
			proc = subprocess.Popen("php /home/pi/Desktop/callyoutube.php", shell=True, stdout=subprocess.PIPE)
			response = proc.stdout.read()
			
			#check if response is valid
			#start the camera and stream!
				
			print('Button Pressed')
			i = 1
	elif i == 2:
		#check if button pressed more than 3 seconds
		if time.time() - start > 3:
			#send terminate signal
			print('End')
			print(time.time())
			print('3 sec')
			x = 0
	else:
		#if input_state == False:
		i = 2
		start = time.time();
		