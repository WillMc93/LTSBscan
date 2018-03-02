import nmap
from itertools import product

IP = ""

# Initalize scanner
nm = nmap.PortScanner()

# Build list of available hosts
available = list()
print("Discovering Hosts (this might take awhile) . . .")

nm.scan(IP, arguments = '-sn -T2 -n --open')
print(len(nm.all_hosts()), " hosts found. Beginning finger printing . . .")

# Fingerprint the hosts
for tgtHost in nm.all_hosts():
	print("Scanning {} . . .".format(tgtHost))
	# Scan the target
	nm.scan(tgtHost, arguments="-T2 -O")

	# If we can detect the OS, . . .
	if 'osmatch' in nm[tgtHost]:
		for match in nm[tgtHost]['osmatch']:
			# Print the first Windows match
			if 'Windows' in match['name']:
				print("OS: {}, accuracy {}%".format(match['name'], match['accuracy']))
				print("MAC: {}".format(nm[tgtHost]['addresses']['mac']))
				break
	else:
		print("No OS match")
