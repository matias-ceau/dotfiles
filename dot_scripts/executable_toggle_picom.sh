 #!/bin/bash

 # Check if picom is running
 if pgrep -x "picom" > /dev/null
 then
     echo "Picom is running. Stopping picom..."
     pkill picom
 else
     echo "Picom is not running. Starting picom..."
     picom -b
 fi
