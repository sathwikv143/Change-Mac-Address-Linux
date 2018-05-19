#!/usr/bin/python

import argparse, os

ifaces = os.listdir('/sys/class/net/')
i = '|'.join(ifaces)
modes = ["random","show","old"]
m = '|'.join(modes)

parser = argparse.ArgumentParser(description="This is to changes mac address of your interfaces", usage = '\nchangemac -i|--iface <interface> -m|--mode <mode>\nInterfaces: %s\nModes: %s\n'% (i,m))
parser.add_argument('-i','--iface', help='Interface name: %s'%i,required=True)
parser.add_argument('-m','--mode',help='Run mode: %s'%m, required=True)
args = parser.parse_args()

inface = args.iface
mmode = args.mode

if inface in ifaces and mmode in modes:
	if mmode=="random":
		os.system("service network-manager stop")
		os.system("macchanger -r %s" % inface)
		os.system("service network-manager start")
	elif mmode=="show":
		os.system("macchanger -s %s" % inface)
	elif mmode=="old":
		os.system("service network-manager stop")
		os.system("macchanger -p %s" % inface)
		os.system("service network-manager start")
	else:
		print("Use correct parameters")
else:
	print("Enter correct interfaces: %s\nUse correct modes: %s" % (i,m))