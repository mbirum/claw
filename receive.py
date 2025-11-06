import pexpect
import time
import sys
import os

ofile = open('output.txt', 'w')
child = pexpect.spawn('bluetoothctl', encoding='utf-8')
child.expect("#")
print('bluetooth started')
child.sendline('default-agent')
child.expect('Default agent request successful')
child.sendline('power on')
child.expect('Changing power on succeeded')
print('agent powered on')
time.sleep(10)
child.expect('Connected: yes')
print('Connected')
child.sendline('menu gatt')
child.expect('Menu gatt')
child.sendline('select-attribute 00002a6e-0000-1000-8000-00805f9b34fb')
child.expect('#')
time.sleep(1)
child.logfile = ofile
while True:
    child.sendline('read')
    variable = child.expect(["\d{2}\s\d{2}"])
    child.expect('#')
    time.sleep(3)
    os.system("cat output.txt | grep -P '\d{2}\s\d{2}' | tail -n 1 | cut -d'#' -f 2 | awk '{print $4}' > value.txt")
