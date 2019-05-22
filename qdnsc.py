from os import system
from subprocess import Popen, PIPE

def banner():
	print "*"*25
	print "Simple DNS Changer"
	print "by: QiubyZhukhi"
	print "Maafkan Akoooh yg pakai 2 Modul gobloknya akuuh"
	print "*"*25+"\n"

terminal = [
	"setprop dhcp.tiwlan0.dns1",
	"setprop dhcp.tiwlan0.dns2",
	"setprop net.ppp0.dns1",
	"setprop net.ppp0.dns2",
	"setprop net.dns1",
	"setprop net.dns2",
	"setprop net.rmnet0.dns1",
	"setprop net.rmnet0.dns2",
	"setprop net.pdpbr1.dns1",
	"setprop net.pdpbr1.dns2"
	]

def dnschanger(d):
	start = [system(i+" "+d) for i in terminal]
	getprops = [i.replace("setprop", "getprop") for i in terminal]
	for i in getprops:
		command, args = i.split(" ")
		com = Popen([command, args], stdout=PIPE).communicate()[0]
		com = str(com).replace("\n", "")
		if com == d:
			print "DNS ON {} Change to {}".format(args, d)
		else:
			print "DNS ON {} Not Change to {}".format(args, d)

def start():
	banner()
	dnssettings = raw_input("Insert DNS: ")
	dnschanger(dnssettings)

if __name__ == "__main__":
	start()
