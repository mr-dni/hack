from requests import get
from rubika.client import Bot
from requests import get
from re import findall
from rubika import Bot
import time
from colorama import Fore,init
from pyfiglet import Figlet

print(Fore.GREEN+ "\n L o a d i n g . . . ")
time.sleep(0.1)
print("")

print ("__________")
time.sleep(0.7)
print (">_________")
time.sleep(0.6)
print (">>________")
time.sleep(0.5)
print (">>>_______")
time.sleep(0.4)
print (">>>>______")
time.sleep(0.3)
print (">>>>>_____")
time.sleep(0.2)
print (">>>>>>____")
time.sleep(0.1)
print (">>>>>>>___")
time.sleep(0.5)
print (">>>>>>>>__")
time.sleep(0.1)
print (">>>>>>>>>_")
time.sleep(0.5)
print (">>>>>>>>>>")
time.sleep(0.1)
print ("UNLOCKED :>")
print ("")

Limpar = "clear"

Sa=Figlet(font="slant")
print(Fore.BLUE+Sa.renderText("nofozer"))
print("")

print(Fore.GREEN+ "\n version 1.0.0 ")
print("")

print(Fore.YELLOW+"\n CODED BY : DANIEL ")
print("")

print(Fore.BLUE+"\n Rubika --> @E3TEFEN ")
print("")

Sa=Figlet(font="slant")
print(Fore.RED+Sa.renderText("MR-DANIEL"))
print("")
auth = input("ENTER YOUR AUTH --->>> \n")

bot = Bot("AppName", auth=auth)

while True:
	try:
		sms = input()
		if sms == ("join"):
			link = input("ENTER YOUR LINK GRUP --->>> \n")
			data = bot.joinGroup(link)
			data = data['data']['group']['group_guid']
		if sms == ("pyam"):
			text = input("ENTER YOUR TEXT MESSAGE --->>> \n")
			bot.sendMessage(data,text)
		if sms == ("left"):
			bot.leaveGroup(data)
		if sms == ("profile"):
			url = input("ENTER YOUR ADRS FILE --->>> \n")
			tar = input("ENTER YOUR GUID ACC --->>> \n")
			bot.uploadAvatar(tar,url)
		if sms == ("block"):
			p = input("ENTER YOUR GUID ACC --->>> \n")
			bot.block(p)
		if sms == ("unblock"):
			r = input("ENTER YOUR GUID ACC --->>> \n")
			bot.unblock(r)
		if sms == ("send pic"):
			m = input("ENTER YOUR ADRS FILE --->>> \n")
			bot.sendPhoto(data,m)
		if sms == ("pyam pv"):
			mtn = input("ENTER YOUR TEXT MESSAGE --->>> \n")
			pv = input("ENTER YOUR GUID ACC --->>> \n")
			bot.sendMessage(pv,mtn)
		if sms == ("send pic pv"):
			msr = input("ENTER YOUR ADRS FILE --->>> \n")
			gg = input("ENTER YOUR GUID ACC --->>> \n")
			bot.sendPhoto(gg,msr)
		if sms == ("send file"):
			mas = input("ENTER YOUR ADRS FILE --->>> \n")
			bot.sendDocument(data,mas)
		if sms == ("send file pv"):
			mss = input("ENTER YOUR ADRS FILE --->>> \n")
			vp = input("ENTER YOUR GUID ACC --->>> \n")
			bot.sendDocument(vp,mss)
		if sms == ("bio"):
			bio = input("ENTER YOUR NEW BIO --->>> \n")
			bot.editProfile(bio= bio)
		if sms == ("name"):
			name = input("ENTER YOUR NEW NAME --->>> \n")
			bot.editProfile(first_name= name)
		print("DONE")
	except:
		print("EROR")