#!/usr/bin/python
import subprocess

#PIPING COMMANDS
p1 = subprocess.Popen(['ls', '-s'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['grep', '.py'], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()

out,err = p2.communicate()

print "\n",out

Capabilities1 = '0x0F'


def int2bin(i):
    if i == '0x0F': return 0x0F


#print int2bin(Capabilities1)

def on_off(i):
    if i == '1':return True
    else: return False
    print i

First, Second, Third, Fourth, Fifth, Sixth, Seventh, Eight = '0'*8
D = {'Values': [First, Second, Third, Fourth, Fifth, Sixth, Seventh, Eight] }


scale = 16
num_of_bits = 8
test = bin(int('0x0F', scale))[2:].zfill(num_of_bits)
test = test[::-1]
print test

#print test[5]
#print on_off(test[1])

step = 0
for num_of_bits in test:
    if on_off(test[step]) == True:
        D['Values'][step] = True
        print D['Values'][step]
    else:
        D['Values'][step] = False
        print D['Values'][step]
    step = step + 1

print '-'*len('hello')

mask = 0b01111111
byte_from_file = 0b10101010
value = mask & byte_from_file
#print bin(value)

byteval = 0x0F
idx = 1

def get_bit(byteval,idx):
    return ((byteval&(1<<idx))!=0);
#print get_bit(byteval,idx)
