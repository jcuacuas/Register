#!/usr/bin/python
import subprocess

#PIPING COMMANDS
p1 = subprocess.Popen(['ls', '-s'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['grep', '.py'], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()

out,err = p2.communicate()

print "\n",out
