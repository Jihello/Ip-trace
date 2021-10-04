import time
c = input("\033[1;32;40m Enter Onion --> ")
time.sleep(1.5)
print("\033[1;32;40m _______    _____ \033[1;34;40m   _______  ______        __       ______   _______\n")
time.sleep(1.5)
print("\033[1;32;40m    |       |    \ \033[1;34;40m     |     |_____\\     /____\\   /         |_______       ")
time.sleep(1.5)
print("\033[1;32;40m    |       |---- \033[1;34;40m      |     |      \\   /      \\  |         |")
time.sleep(1.5)
print("\033[1;32;40m _______    | \033[1;34;40m          |     |       \\ /        \\ \\_______  ________\n")
time.sleep(3)
print("\033[1;32;40m __________")
print("\033[1;32;40m| \033[1;34;40mIP \033[1;32;40mTRACE |")
print("|__________|")
time.sleep(2)
print("\033[1;33;40m LODING.....\n")
time.sleep(3)
print("\033[1;33;40m WAIT FEW MINUTES\n")
time.sleep(5)
print("\033[1;31;40m Loding..........................................(/)10%")
time.sleep(2.5)
print("\033[1;31;40m Loding..........................................(\)15%")
time.sleep(2.5)
print("\033[1;31;40m Loding..........................................(/)25%")
time.sleep(5)
print("\033[1;31;40m Loding..........................................(\)50%")
time.sleep(3)
print("\033[1;31;40m Loding..........................................(/)70%")
time.sleep(2.5)
print("\033[1;31;40m Loding..........................................(\)85%")
time.sleep(5)
print("\033[1;31;40m Loding..........................................(/)98%")
time.sleep(10)
print("\033[1;31;40m Loding..........................................(\)100%")
time.sleep(5)
print("\033[1;34;40m Loding succesfull please wait few second\n")
time.sleep(2.5)
print("\033[1;34;40mLoding succesfull please wait few second....\n")
time.sleep(3)
n = input("\033[1;31;40mEnter mobile number :")
time.sleep(10)
print("\033[1;31;40mInformation is collected")
e = input("\033[1;32;40mPlease Enter :\n")
time.sleep(2.5)
print("\033[1;31;40m1. [IP ADDRESS]")
time.sleep(2.5)
print("\033[1;32;40m2. [FULL INFO]")
time.sleep(2.5)
print("\033[1;36;40m3. [EXIT]\n")
def xyz(x):
	switcher={
	1:"\033[1;31;40mIP Adress : 125.00.789.543",
	2:"\033[1;31;40mName : Adnan Ansari"
 "\033[1;31;40mAddres : Utar pradesh HM-43/500E Gali No-14 District Iklendi Ganv "
"\033[1;31;40mAge : 22",
    3:"exit",
	}
	return switcher.get(x,"option is default")
	
n=int(input("Enter choice: "))
c=xyz(n)
print(c)
	








