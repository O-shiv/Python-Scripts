#!/usr/bin/env python
#Author: Shivesh Ojha

import subprocess  #to call linux commands
import time        #to give a time lag
import optparse    #to parse output in the terminal
import re          #to check regex

subprocess.call("figlet MAC CHANGER", shell=True)

def get_arguments():
	parser = optparse.OptionParser(usage="This tool helps to change the mac address of the given interface")
	parser.add_option("-i", dest="interface", help="interface to change its mac address")
	parser.add_option("-m", dest="new_mac", help="new mac address")
	(options, arguments) = parser.parse_args()
	if not options.interface:
		parser.error("[-] Please specify an interface, use --help for more info")
	elif not options.new_mac:
		parser.error("[-] Please specify a new mac address, use --help for more info")
	return options

def change_mac(interface, new_mac):
	subprocess.call("ifconfig "+interface+" down", shell=True)
	subprocess.call("ifconfig "+interface+" hw ether "+new_mac, shell=True)
	subprocess.call("ifconfig "+interface+" up", shell=True)

	print("[+] Changing MAC address for "+interface+" to "+new_mac)
	time.sleep(1)

def get_mac(interface):
	result = (subprocess.check_output(["ifconfig", options.interface]))
	mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", result)

	if mac_address:
		return mac_address.group(0)
	else:
		print("[-] Could not change MAC Address")

options = get_arguments()

current_mac = get_mac(options.interface)
print("Current MAC = "+str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_mac(options.interface)

if (current_mac == options.new_mac):
	print("[+] MAC address successfully changed to "+current_mac)
else:
	print("[-] Could not change MAC Address")