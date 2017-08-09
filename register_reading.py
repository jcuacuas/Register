#!/usr/bin/python
import subprocess

dimms = ['dim2', 'dim1'] #AN ATTEMPT TO READ MULTIPLE REGISTERS
for index in range(len(dimms)):

    cmd = "awk '/0x00/ { print $7; }' ../../Registers.txt "  #READ THE REGISTER FROM TEXT FILE

    proc = subprocess.Popen(cmd, shell=True,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #EXECUTE CMD. REDIRECT COMMAND OUTPUT AND ERROR TO PIPE FOR LATER USE
    out,err = proc.communicate()
    #WAIT FOR COMMAND TO FINISH. RETURN COMMAND OUTPUT AND ERROR WHEN FINISHED

    var = out #READS OUT DESCRIPTION, DEPENGING ON VALUE
    var = var.rstrip()

    if err != "":
        print err
    elif var == "0" :
        print "Current page number:0"
    elif var == "1" :
        print "Current page number:1"
    else:
        print "nothing to see"

        break

#READING MULTIPLE REGISTERS USING HASHING

cmd1 = "awk '/0x00/ { print $7; }' ../../Registers.txt "
proc1 = subprocess.Popen(cmd1 , shell=True,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out1,err = proc1.communicate()

print "\n" , out1
out1 = out1.rstrip()

cmd2 = "awk '/0x01/ { print $7; }' ../../Registers.txt "
proc2 = subprocess.Popen(cmd2 , shell=True,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out2,err = proc2.communicate()

print "\n" , out2
out2 = out2.rstrip()

cmd3 = "awk '/0x02/ { print $7; }' ../../Registers.txt "
proc3 = subprocess.Popen(cmd3 , shell=True,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out3,err = proc3.communicate()

print "\n" , out3
out3 = out3.rstrip()

cmd4 = "awk '/0x10/ { print $7; }' ../../Registers.txt "
proc4 = subprocess.Popen(cmd4 , shell=True,  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out4,err = proc4.communicate()

print "\n" , out4
out4 = out4.rstrip()

if out4 == "02":
    print "hello"

D = {}
D['0x00'] = 'Current page number: ' + out1
D['0x01'] = 'Highest number of a page that is supported by the module: ' + out2
D['0x02'] = 'Vendor pages start at: ' + out3
D['0x10'] = out4

for register,output in D.items():
    print register,':',output

print err

def increment(number):
        return number + 0x01

N = 0x02
for i in xrange(N):
    print increment(0x10)

d = {}
d['lunch'] = {}
d['breakfast'] = {}
d['lunch']['ham'] = 'cheese'
d['breakfast']['eggs'] = 'bacon'


for part1,part2 in d.items():
    for part2,part3 in d.items():
        print part1,'=',part3,':',part2 
