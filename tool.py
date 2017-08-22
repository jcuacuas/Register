#!/usr/bin/python
import subprocess

#METHOD USED TO PIPE IICMASTER TO GREP
cmd1 = 'makespsystemcall -raw "iicmaster -b /dev/iic/L02C0E06P14 -s -a 0x80 -o 0x00 -r 1"'
cmd2 = 'grep -v [:digit:]'

p1 = subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
p2 = subprocess.Popen(cmd2, stdin=p1.stdout, shell=True, stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
#THIS COMMAND MAY NOT BE NECCESSARY
p1.stdout.close()

out,err = p2.communicate()

#DEFINING OFFSETS
#NUMBER VALUES ARE REPLACED BY CMD
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
Capabilities0 = '0F'
Capabilities1 = '01'
Energy_Source_Policy = '03'

#IF STATEMENTS ARE USED TO DETERMINE CERTAIN OFFSET DESCRIPTIONS
#VARIABLES MUST BE SET TO A BLANK STRING
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

#MORE OFFSET DESCRIPTIONS
Current_Page_Des = 'Current Page'
Max_Pages_Des = 'Highest number of a page that is supported by the module: '
Vendor_Num_Des = 'The number of vendor-specific pages supported: '
Hard_Rev_Des = 'Controller hardware revision: '
Slot0_Fwrev0_Des = 'Slot 0 controller firmware revision, least significant byte: '
Slot0_Fwrev1_Des = 'Slot 0 controller firmware revision, most significant byte: '

#VALUES AND VALUE_DES MUST BE ADDED TO BE DISPLAYED
D = {'Registers': [Current_Page, Max_Pages,
    Vendor_Start_Pages, Vendor_Num_Pages,
    Hard_Rev, Specrev, Slot0_Fwrev0, Slot0_Fwrev1, Slot1_Fwrev0,
    Slot1_Fwrev1, Slot0_Subfwrev, Slot1_Subfwrev],
 'Descriptions' : [Current_Page_Des, Max_Pages_Des,
    Vendor_Start_Des, Vendor_Num_Des,
    Hard_Rev_Des, Specrev_Des, Slot0_Fwrev0_Des, Slot0_Fwrev1_Des,
    Slot1_Fwrev0_Des, Slot1_Fwrev1_Des, Slot0_Subfwrev_Des,
    Slot1_Subfwrev_Des] }

#DISPLAYING METHOD THAT USES DICTIONARIES
step = 0
for i in D['Registers']:
<<<<<<< HEAD
    #ORGANIZING THE DISPLAY
=======
>>>>>>> f421ecaf34c81391a1473b0abe0cae8dd177eb8f
    if step == 0:
        x = 'Paging Mechanism Registers'
        print '-'*len(x) + '\nPaging Mechanism Registers \n'+ '-'*len(x)
    if step == 4:
        x = 'Version Registers'
        print '-'*len(x) + '\nVersion Registers \n'+ '-'*len(x)
    print D['Descriptions'][step],D['Registers'][step]
    step = step + 1

x = 'Characteristics Registers'
print '-'*len(x) + '\nCharacteristics Registers \n'+ '-'*len(x)

<<<<<<< HEAD
#MORE COMPLEX OFFFSET READING
=======
>>>>>>> f421ecaf34c81391a1473b0abe0cae8dd177eb8f
def on_off(i):
    if i == '1':return True
    else: return False
    print i

First, Second, Third, Fourth, Fifth, Sixth, Seventh, Eight = '0'*8
D = {'Values': [First, Second, Third, Fourth, Fifth, Sixth, Seventh, Eight] }


scale = 16
num_of_bits = 8
num_of_bits1 = 4
<<<<<<< HEAD
#TURN THE HEX STRING INTO BINARY STRING
Capabilities0_Test = bin(int(Capabilities0, scale))[2:].zfill(num_of_bits)
#REVERSE THE BITS
Capabilities0_Test = Capabilities0_Test[::-1]

#SEPERATE THE BITS AND DETERMINE WHETHER THE BIT IS ON OR NOT
=======
Capabilities0_Test = bin(int(Capabilities0, scale))[2:].zfill(num_of_bits)
Capabilities0_Test = Capabilities0_Test[::-1]

>>>>>>> f421ecaf34c81391a1473b0abe0cae8dd177eb8f
step = 0
for num_of_bits in Capabilities0_Test:
    if on_off(Capabilities0_Test[step]) == True:
        D['Values'][step] = 1
    else:
        D['Values'][step] = 0
    step = step + 1

<<<<<<< HEAD
#IF THE BIT IS ON: PRINT DESCRIPTION
=======
>>>>>>> f421ecaf34c81391a1473b0abe0cae8dd177eb8f
print '\n' + '-'*5 + ' CAPABILITIES0 - Offset0x10 ' + '-'*5 + '\n'
if D['Values'][0]:
    print 'Module supports asserting the EVENT_n pin when an enabled event occurs'
if D['Values'][1]:
    print 'Module performs periodic Energy Source health checks'
if D['Values'][2]:
    print 'Module supports error injection'
if D['Values'][3]:
    print 'Module supports collecting the device statistics'
if D['Values'][4]:
    print 'Module supports I2C Block Read transactions and I2C Block Write transactions for Typed Block Data'
if D['Values'][5]:
    print 'Module supports two-pulse SAVE_n trigger mode'
if D['Values'][6]:
    print 'Module supports three-pulse SAVE_n trigger mode'
if D['Values'][7]:
    print 'Module supports the LCOM interface'

<<<<<<< HEAD
=======


>>>>>>> f421ecaf34c81391a1473b0abe0cae8dd177eb8f
scale = 16
num_of_bits = 8
num_of_bits1 = 4
Capabilities1_Test = bin(int(Capabilities1, scale))[2:].zfill(num_of_bits)
Capabilities1_Test = Capabilities1_Test[::-1]

step = 0
for num_of_bits in Capabilities1_Test:
    if on_off(Capabilities1_Test[step]) == True:
        D['Values'][step] = 1
    else:
        D['Values'][step] = 0
    step = step + 1

print '\n' + '-'*5 + ' CAPABILITIES1 - Offset0x11 ' + '-'*5 + '\n'
if D['Values'][0]:
    print 'Module supports the Atomic Arm and Erase operation'
if D['Values'][1]:
    print 'ABORT_CMD_TIMEOUT register is in units of seconds'
if not D['Values'][1]:
    print 'ABORT_CMD_TIMEOUT register is in units of milliseconds'
if D['Values'][2]:
    print 'Module supports an Operational Unit buffer for each Typed Block Data type'
if D['Values'][3]:
    print 'Module supports I2C Word Read transactions and I2C Word Write transactions for Typed Block Data'
if D['Values'][4] == D['Values'][5] == 0:
    print 'Reset Controller operation semantics are not reported'
elif D['Values'][4] == D['Values'][5] == 1:
    print 'Reserved'
elif D['Values'][4]:
    print 'Reset Controller operation honors SAVE_n'
elif D['Values'][5]:
    print 'Reset Controller operation does not honor SAVE_n'

Energy_Source_Policy_Test = bin(int(Energy_Source_Policy, scale))[2:].zfill(num_of_bits1)
Energy_Source_Policy_Test = Energy_Source_Policy_Test[::-1]
step = 0
for num_of_bits1 in Energy_Source_Policy_Test:
    if on_off(Energy_Source_Policy_Test[step]) == True:
        D['Values'][step] = 1
    else:
        D['Values'][step] = 0
    step = step + 1

<<<<<<< HEAD
#DISPLAY ORGANIZATION
=======
>>>>>>> f421ecaf34c81391a1473b0abe0cae8dd177eb8f
print '\n' + '-'*5 + ' ENERGY_SOURCE_POLICY_TEST - Offset0x14 ' + '-'*5 + '\n'

if D['Values'][0]:
    print 'Device Managed Policy supported'
if D['Values'][1]:
    print 'Host Managed Policy supported'

print '\n' + '-'*5 + ' HOST_MAX_OPERATION_RETRY - Offset0x15 ' + '-'*5 + '\n'
