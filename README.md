Custom Python TCP reverse Shell for PWK course

Start Apache2 webserver

Add the ClientTCPreverseShell to a zip file and copy to your /var/www/http

two files

1. ClientTCPreverseShell
2. ServerTCPreverseShell

usage
On Kali - python ServerTCPreverseShell.py
On remote client - python ClientTCPreverseShell.py


Exfil data
grab*exfil_data.txt

Convert "ClientTCPrevshell" to EXE format. 
Get py2exe for windows and make sure to get the correct python versian.
https://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/
copy to your var/www/html folder and upload to your windows 7 machine.

Upload the ClientTCPreverseShell to the custom windows 7 machine

Install py2exe and then move the py2exe program into the same folder as 
ClientTCPreverseShell and setup.py


Edit setup.py with idle by right clicking and edit with idle. 

then run module

then test your new custom python exe shell. Copy the exe from the "dist" folder
to the desktop and start the server on kali.

Then zip up your new custom EXE python shell and from the python server on kali

Shell> grab*Clientshell.zip

now go to your desktop and rename test.txt to ClientShell.zip

Works for me and will work for you!!!





