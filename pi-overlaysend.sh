#!/bin/bash
# Get the temps from the get_temp.py script output
n=( $(/home/pi/get_temp.py ) )
TEMPERATURE=${n[0]}
TEMPERATUREF=${n[1]}
# If you are using wifi and want the signal quality in the display
q=( $(/sbin/iwconfig wlan0 | grep -i quality | awk '{ print $2}'| sed s/Quality=//g | sed 's/\/100//g') )
VQUAL=${q[0]}
# If you want to read the RPI CPU temp and have it displayed
p=( $( /home/pi/read_pi_cpu_temp.sh | sed 's/temp=//g'| sed s/\'C//g ) )
PITEMP=${p[0]}
# Display the 3 items on the bottom left of the pi camera screen
/usr/bin/wget -q --delete-after "http://admin:YOURPASSWORD@localhost:7999/1/config/set?text_left=cput:$PITEMP\ntemp:$TEMPERATURE\nqual:$VQUAL"
# If you want to update your Wunderground PWS Station
/usr/bin/wget -q --delete-after "http://rtupdate.wunderground.com/weatherstation/updateweatherstation.php?ID=YOURSTATIONID&PASSWORD=YOURPASSWORD&dateutc=`date +'%F %T'`&tempf=$TEMPERATUREF&softwaretype=rpi%20version1.1&action=updateraw&realtime=1&rtfreq=120"
