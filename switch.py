from time import sleep
import RPi.GPIO as GPIO
import subprocess


#define all the pin number
blinkLed = 3;
pushButton = 11

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pushButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(blinkLed, GPIO.OUT)
GPIO.output(blinkLed,GPIO.LOW)

record = 0
buttonPressed = 0
blink = 'high'
x = 1;
while x > 0:
	#get input from pin pushButton
	input_state = GPIO.input(pushButton)
	
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
				
				GPIO.output(blinkLed,GPIO.HIGH)
			else:
				GPIO.PWM(blinkLed,100)
				if blink == 'high':
					GPIO.output(blinkLed,GPIO.HIGH)
					blink = 'low'
				else:
					GPIO.output(blinkLed,GPIO.LOW)
					blink = 'high'
				
		else:
			#if recording has started and button being press more than 3 seconds. Stop recording
			if buttonPressed > 3:
				proc = subprocess.Popen("php /home/pi/Desktop/disconnect.php", shell=True, stdout=subprocess.PIPE)
				response = proc.stdout.read()
				print('Stop Recording')
				record = 0
				buttonPressed = 0
	sleep(1) #sleep for 1 second				
	#GPIO.cleanup()