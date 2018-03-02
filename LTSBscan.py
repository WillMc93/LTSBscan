import nmap
from itertools import product

IP = ""

# Initalize scanner
nm = nmap.PortScanner()


# Build list of available hostnames
available = list()
print("Discovering Hosts . . .")

nm.scan(IP, arguments = '-sn -T2 polite --open')
available = nm.all_hosts()


print(available)

# Scan
for tgtHost in available:
	print("Scanning {}".format(tgtHost))
	# Scan the target
	nm.scan(tgtHost, arguments="-O -T polite")

	# If we can detect the OS, . . .
	if 'osmatch' in nm[tgtHost]:
		for match in nm[tgtHost]['osmatch']:
			# Print the first Windows match
			if 'Windows' in match['name']:
				print("OS: {}, accuracy {}".format(match['name'], match['accuracy']))
				print("MAC: {}".format(nm[tgtHost]['addresses']['mac']))
				break
	else:
		print("No OS match")
