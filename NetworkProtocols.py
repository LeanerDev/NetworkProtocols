import os
import sys
from time import sleep


def AsciiArt():
	print("\n")
	print("""
▄───▄
█▀█▀█
█▄█▄█
─███──▄▄
─████▐█─█ By: Leaner#4241
─████───█
─▀▀▀▀▀▀▀""")

def menu():
	print("""
	[1] protocol data
	[2] all TCP connections
	[3] all UDP connections
	[4] all TCP and UDP connections
	[5] Information routing
        [6] Create message server
        [7] Send file
    
	""")
AsciiArt()
menu()

print("\n")

network = input("Choose an option:")
if network == "1":
	os.system("netstat -s")
elif network == "2":
	os.system("netstat -at")
elif network == "3":
	os.system("netstat -au")
elif network == "4":
	os.system("netstat -aut")
elif network == "5":
	os.system("netstat -rn")
elif network == "6":
	port = input("type a port:")
	os.system("nc -l -vv -p {}".format(port))
elif network == "7":
	port = input("type port:")
	archive = input("file name:")
	os.system("nc -nlvp  {} < {}".format(port,archive))

	
	

	
sleep(2)
print("""
 )  (
     (   ) )
      ) ( (
 _______)_
 .-'---------|  
( C|/\/\/\/\/|Até a próxima amigo!
 '-./\/\/\/\/|
   '_________'
    '-------'""")
