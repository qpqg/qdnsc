from subprocess import Popen,PIPE

def banner():
	grs = "="*20
	return "{}\nDNS Changer\nby: QiubyZhukhi\n{}".format(grs,grs)

def grep(command):
	return Popen([command],shell=True ,stdout=PIPE).communicate()

def check_dns():
	return str(grep("getprop|grep dns")[0]).replace("[","").replace("]","")
	
def dns_changers(f, s):
	ment = ["net.dns1",
			"net.dns2",
			"net.rmnet_data0.dns1",
			"net.rmnet_data0.dns2",
			"net.ppp0.dns1",
			"net.ppp0.dns2"]
	for commands in check_dns().split("\n"):
		commands = commands.split(":")[0]
		if commands in ment:
			akhir = int(commands[-1])
			if akhir == 1:
				grep("setprop " + commands + " " + f)
			elif akhir == 2:
				grep("setprop "+ commands + " "+s)
	print "==== NOW YOURS DNS ===="
	print check_dns()
	print "======================="
def main():
	print banner()
	list_menus = {"google dns":["8.8.8.8/8.8.4.4"],
			"Norton ConnectSafe":["199.85.126.10/199.85.127.10"],
			"Open DNS":["208.67.222.222/208.67.220.220"],
			"DNS Watch":["84.200.69.80/84.200.70.40"],
			"Comodo Secure DNS": ["8.26.56.26/8.20.247.20"],
			"Veri Sign":["64.6.64.6/64.6.65.6"],
			"Open NIC":["192.95.54.3/192.95.54.1"],
			"Green TeamDNS":["81.218.119.11/209.88.198.133"]
			}

	print "===== [ ORIGINAL DNS ] ===="
	print check_dns()
	n = 0
	for i, (v) in list_menus.items():
		n += 1
		print "[{}]. {}".format(n,i)
	print "[ Enter ] for setting manual DNS"
	try:
		ops = int(raw_input("Insert: "))-1
		print "Setting to Dns [{}]".format(list_menus.items()[ops][0])
		f,s = list_menus.items()[ops][1][0].split("/")
		dns_changers(f,s)
	except Exception:
		print "Use example: 8.8.8.8/8.8.4.4"
		forstdns, seconddns = raw_input("Insert DNS: ").split("/")
		dns_changers(forstdns, seconddns)
	
if __name__ == "__main__":
	main()
	
