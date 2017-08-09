#!/usr/bin/python
import subprocess

#PIPING COMMANDS
cmd1 = 'makespsystemcall -raw "iicmaster -b /dev/iic/L02C0E06P14 -s -a 0x80 -o 0x00 -r 1"'
cmd2 = 'grep -v [:digit:]'

p1 = subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
p2 = subprocess.Popen(cmd2, stdin=p1.stdout, shell=True, stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
p1.stdout.close()

out,err = p2.communicate()

Current_Page = '00'
Max_Pages = '04'
Vendor_Start_Pages = '04'
Vendor_Num_Pages = '01'
Hard_Rev = '5c'
Specrev = '21'
Slot0_Fwrev0 = '20'
Slot0_Fwrev1 = '00'
Slot1_Fwrev0 = '00'
Slot1_Fwrev1 = '00'
Slot0_Subfwrev = '00'
Slot1_Subfwrev = '00'

if Vendor_Start_Pages == Max_Pages:
    Vendor_Start_Des = 'There are no vendor pages'
    Vendor_Start_Pages = ''
else :
    Vendor_Start_Des = 'Vendor pages start at'

if Specrev == '10':
    Specrev_Des = 'Revision: JESD245'
    Specrev = ''
elif Specrev == '20':
    Specrev_Des = 'Revision: JESD245A'
    Specrev = ''
elif Specrev == '21':
    Specrev_Des = 'Revision: JESD245B'
    Specrev = ''

if Slot1_Fwrev0 == '00':
    Slot1_Fwrev0_Des = 'Slot 1 does not contain a firmware image or contains an invalid firmware image'
    Slot1_Fwrev0 = ''
else:
    Slot1_Fwrev0_Des = 'Slot 1 controller firmware revision, least significant byte'

if Slot1_Fwrev1 == '00':
    Slot1_Fwrev1_Des = 'Slot 1 does not contain a firmware image or contains an invalid firmware image'
    Slot1_Fwrev1 = ''
else:
    Slot1_Fwrev1_Des = 'Slot 1 controller firmware revision, most significant byte'

if Slot0_Subfwrev == '00':
    Slot0_Subfwrev_Des = 'No subcomponent firmware image in slot 0'
    Slot0_Subfwrev = ''
else:
    Slot0_Subfwrev_Des = 'Subcomponent firmware revision of the firmware image in slot 1: '

if Slot1_Subfwrev == '00':
    Slot1_Subfwrev_Des = 'No subcomponent firmware image in slot 1'
    Slot1_Subfwrev = ''
else:
    Slot1_Subfwrev_Des = 'Subcomponent firmware revision of the firmware image in slot 1: '

Current_Page_Des = 'Current Page'
Max_Pages_Des = 'Highest number of a page that is supported by the module: '
Vendor_Num_Des = 'The number of vendor-specific pages supported: '
Hard_Rev_Des = 'Controller hardware revision: '
Slot0_Fwrev0_Des = 'Slot 0 controller firmware revision, least significant byte: '
Slot0_Fwrev1_Des = 'Slot 0 controller firmware revision, most significant byte: '

D = {'Registers': [Current_Page, Max_Pages,
    Vendor_Start_Pages, Vendor_Num_Pages,
    Hard_Rev, Specrev, Slot0_Fwrev0, Slot0_Fwrev1, Slot1_Fwrev0,
    Slot1_Fwrev1, Slot0_Subfwrev, Slot1_Subfwrev],
 'Descriptions' : [Current_Page_Des, Max_Pages_Des,
    Vendor_Start_Des, Vendor_Num_Des,
    Hard_Rev_Des, Specrev_Des, Slot0_Fwrev0_Des, Slot0_Fwrev1_Des,
    Slot1_Fwrev0_Des, Slot1_Fwrev1_Des, Slot0_Subfwrev_Des,
    Slot1_Subfwrev_Des] }

step = 0
for i in D['Registers']:
    print D['Descriptions'][step],D['Registers'][step]
    step = step + 1
