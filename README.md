## motioneye-tools
A few scripts that will enhance the use of motioneye on raspberry pi using GPIO sensors


#motioneye-tools

A few scripts that will enhance the use of motioneye on raspberry pi using GPIO sensors

**pi_overlaysend.sh**


This script is designed for those using the waterproof outdoor temperature sensor DS18B20

It will detect the device, parse the temperature and display on the motioneye overlay (left frame). This will replace
the camera-name field.

**Requirements:**

 - Raspberry Pi Model A, B, B+ or Raspberry Pi 3 

 - Pi Camera Board with cable (This should work with v2, but I have not tested it)
	 - https://www.raspberrypi.org/products/camera-module/  

 - DS18B20 Digital Waterproof temperature sensor
	 - https://www.adafruit.com/product/381 

 - MotionEye software
     - https://github.com/ccrisan/motioneye
 
 - Rasbian or Linux os for your Raspberry Pi that supports 1 Wire
   Interface over GPIO

 
 - A working version of Python installed

**Software setup**

 - Download and install Raspbian Lite
		https://www.raspberrypi.org/downloads/raspbian/
			apt-get update ; apt-get upgrade ; apt-get dist-upgrade

 - Install and configure your 1 wire drivers

    https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/overview
    
 - Setup your wired, or wireless networking on the Pi

 - Install MotionEye software and configure.

 - Test your camera and settings (http://CAMERA-IP:8765/)

 **Installing and using pi-overlaysend.sh**
 
  - Copy over the three scripts
    - get_temp.py (this uses the 1wire interface to get F and C Temperatures)
    - read_pi_cpu_temp.sh (this gets the PI CPU Temp for the overlay)
    - pi-overlaysend.sh (the main script, to be run via crontab)
    
  - Add a crontab with the time update you would prefer to call pi-overlaysend.sh
    - /2 * * * * /home/pi/pi-overlaysendscript.sh 2>&1 /dev/null
    

