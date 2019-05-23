from subprocess import Popen,PIPE

def banner():
	print "="*15
	print "Simple Dns Changer"
	print "by: Qiuby Zhukhi"
	print "="*15+"\n"

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
	banner()
	print "===== [ ORIGINAL DNS ] ===="
	print check_dns()
	print "Use example: 8.8.8.8/8.8.4.4"
	forstdns, seconddns = raw_input("Insert DNS: ").split("/")
	dns_changers(forstdns, seconddns)
if __name__ == "__main__":
	main()
	
