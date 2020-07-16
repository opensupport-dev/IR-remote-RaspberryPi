from lirc import RawConnection

def ProcessIRRemote():
       
    #get IR command
    #keypress format = (hexcode, repeat_num, command_key, remote_id)
    #                = 0000000000ffa857 01 KEY_PLAY freeNanum
    try:
        keypress = conn.readline(.0001)
        #print(keypress)
    except:
        keypress=""
              
    if (keypress != "" and keypress != None):
                
        data = keypress.split()
        sequence = data[1]
        command = data[2]
        
        #ignore command repeats
        if (sequence != "00"):
           return
        
        # print "KEY_PLAY"
        print(command)        
            

#define Global
conn = RawConnection()

print("Starting Up...")

while True:         

      ProcessIRRemote()
      