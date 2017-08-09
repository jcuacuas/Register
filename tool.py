#!/usr/bin/python
import subprocess

#PIPING COMMANDS
cmd = 'makespsystemcall -raw "iicmaster -b /dev/iic/L02C0E06P14 -s -a 0x80 -o 0x00 -r 1"'
cmd1 = 'grep -v [:digit:]'

p1 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
p2 = subprocess.Popen(cmd1, stdin=p1.stdout, shell=True, stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
p1.stdout.close()

out,err = p2.communicate()

print out
print err

N = 0x0A
for i in xrange(N):
    print "hello"
