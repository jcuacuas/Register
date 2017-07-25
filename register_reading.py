#!/usr/bin/python
import subprocess

cmd_1 = "awk '/0x00/ { print $7; }' ../Registers.txt "  #READ THE REGISTER

proc = subprocess.Popen(cmd_1, shell=True,  stdout=subprocess.PIPE, stderr=subprocess.PIPE) #EXECUTE CMD. REDIRECT COMMAND OUTPUT AND ERROR TO PIPE FOR LATER USE
out,err = proc.communicate() #WAIT FOR COMMAND TO FINISH. RETURN COMMAND OUTPUT AND ERROR WHEN FINISHED

var = out
var = var.rstrip()

if err != "":
    print err
elif var == "0" :
    print "Current page number:0"
else:
    print "nothing to see"
