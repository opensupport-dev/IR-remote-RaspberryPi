#!/bin/bash

#
# process ir command.
#

#./ir-process-exe.py
./ir-process-exe.py &

#
# play vlc player automatically.
#
./vlc-start.sh

#sleep(1)

#
# process ir command in bg.
#
#./ir-process-exe.py &
#./ir-process-exe.py


