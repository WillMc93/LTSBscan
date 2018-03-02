import nmap
import csv

IP = ''

# Initalize scanner
nm = nmap.PortScanner()

# Build list of available hosts
available = list()
print("Discovering Hosts (this might take awhile) . . .")

nm.scan(IP, arguments = '-sn -T2 -n --open')
print(len(nm.all_hosts()), " hosts found. Beginning finger printing . . .")

# Clear output file
out = open('LTSB.csv', 'w').close

# Open file for writing
with open('LTSB.csv', 'a') as out:
	# start csv writer
	writer = csv.writer(out, delimiter=',')

	# Fingerprint the hosts
	for tgtHost in nm.all_hosts():
		print("Scanning {} . . .".format(tgtHost))
		# Scan the target
		nm.scan(tgtHost, arguments="-O")

		#print(nm[tgtHost]['hostnames'])
		name = nm[tgtHost]['hostnames'][0]['name']
		mac = nm[tgtHost]['addresses']['mac']
		os = ''
		accuracy = ''
		for match in nm[tgtHost]['osmatch']:
			# Get the first Windows match and the accuracy of the match
			if 'Windows' in match['name']:
				os = match['name']
				accuracy = match['accuracy']
				break
		if os == '':
			os = "Probably not Windows"

		# Append output file
		writer.writerow([name, mac, os, accuracy])

print("\n\nDONE!")
