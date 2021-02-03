import os 
from time import sleep
os.system("clear")
print ("PLEASE WAIT")
import amino
os.system("clear")
print("\033[0;31m"+""" _   _ _ _             _____                       
| | | | | |           /  ___|                      
| | | | | |_ _ __ __ _\ `--. _ __   __ _ _ __ ___  """)
print("\033[0;33m"+"""| | | | | __| '__/ _` |`--. \ '_ \ / _` | '_ ` _ \ 
| |_| | | |_| | | (_| /\__/ / |_) | (_| | | | | | |""")
print("\033[0;36m"+""" \___/|_|\__|_|  \__,_\____/| .__/ \__,_|_| |_| |_|
                            | |                    
                            |_|                    """)
print ("\n")
do=("\033[0;33m"+"[DONE]")
num=(0)
attackswhile=(0)
kkkk="كلكم خاضعين تحتنا"
sleep(0.5)
sleep(0.5)
print("\033[0;31m"+"""YOUTUBE:
	Flame""")
sleep(0.5)
print ("\n")
print("\033[0;36m"+ "DARK KING & DASH ©®")
client=amino.Client()
print ("\n")
sleep(0.5)
email=input("\033[0;32m"+"your email : ")
print("\n")
sleep(0.5)
password=input("\033[0;32m"+"your password : ")
print("\n")
try:
	
    client.login(email=email,password=password)
except:
	 print("email or password uncorrect, check it please and try again")
	 sleep(9999)

grouplink=input ("\033[0;33m"+"the link: ")
try:
	gpid=client.get_from_code(grouplink)
	chatid=gpid.objectId
	comid=gpid.path[1:gpid.path.index("/")]
except:
	print ("\n")
	print("the link invaild, kiddo")
	print ("\n")
	sleep(827382)
	
print("\n")
sleep (0.5)
atnumbers=int(input("\033[0;34m"+"attacks number: "))
print("LETS SEE...")
subclient = amino.SubClient(comId=comid, profile=client.profile)
print("\n")

while attackswhile<atnumbers :
	subclient.join_chat(chatId=chatid)
	num+=1
	print(do, num)
	subclient.leave_chat(chatId=chatid)
	num+=1
	print(do,num)
	attackswhile+=2
     
     	
print("\n")
print("\033[0;31m"+"""YOUTUBE:
	Flame""")
print("\033[0;36m"+ "DARK KING & DASH ©®")
print("\n")
os.system("exit()") 
