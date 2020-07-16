#!/bin/bash

#
# freenanum.github.io/market
#
#vlc /home/pi/Videos/*.* --loop

#cvlc /home/pi/Videos/*.* --loop
#cvlc /home/pi/Videos/*.* --video-on-top --loop
#cvlc /home/pi/Videos/*.* --fullscreen --loop


# 1. result: hotkey disabled
#cvlc /home/pi/Videos/ --fullscreen --video-on-top --loop --playlist-autostart #--recursive none

# 2. result: hotkey disabled
#cvlc /home/pi/Videos --video-on-top --loop --playlist-autostart

# 3. result: good
#cvlc /home/pi/Videos --fullscreen --playlist-autostart #--reset-config

# 4. result:
#cvlc /home/pi/Videos --loop --playlist-autostart


# 5. result:
cvlc /home/pi/Videos/*.*

# 6. result: bad
#vlc /home/pi/Videos

#cvlc --fullscreen --video-on-top --loop /home/pi/Videos
#cvlc --fullscreen --video-on-top --autoscale --loop /home/pi/Videos

#cvlc --open /home/pi/Videos/*.* --fullscreen --video-on-top --loop --intf="http" --http-password 3325 --http-host 0.0.0.0 --http-port 8080

