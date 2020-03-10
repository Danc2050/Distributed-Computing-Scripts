#!/usr/bin/python3

# Daniel Connelly
 # based off of Tdulcet's expect script
# Python3 exp.py <User ID> <Computer name> <Type of work>

# NOTE
'''
pexpect does not like nonempty ()s (e.g., (y)), *s, inline ''s, or +s. Try not to use them.
pexpect does not seem to be able to skip over queries with the default or "enter" key.
'''

import sys
import time
import os

# Dependencies
try:
    import pexpect
except ImportError as error:
    p = subprocess.run('pip install pexpect', shell=True)
    import pexpect

# Prerequisites
time.sleep(1)
os.environ["USERID"], os.environ["COMPUTER"], os.environ["TYPE"]  = sys.argv[1], sys.argv[2], sys.argv[3]

# Pexpect script
child = pexpect.spawn('./mprime -m')
child.logfile = sys.stdout.buffer # zartaz's comment: https://github.com/pexpect/pexpect/issues/518

child.expect('Join Gimps?')
time.sleep(1)
child.sendline('y') # another acceptable version: child.send('y\r')
#child.send('y\r')

child.expect("Use PrimeNet to get work and report results ()")
time.sleep(1)
child.sendline("y")
#child.send("y\r")

child.expect("Your user ID or")
time.sleep(1)
child.sendline(os.environ["USERID"])
#child.send(os.environ["USERID"]+"\r")
child.expect("Optional computer name:")
time.sleep(1)
child.sendline(os.environ["COMPUTER"])
#child.send(os.environ["COMPUTER"]+"\r")
child.expect("Computer uses a dial-up connection")
time.sleep(1)
child.sendline("N")
child.expect("Use a proxy server")
time.sleep(1)
child.sendline("N")
child.expect("Output debug info to prime.log")
time.sleep(1)
child.sendline("0")
child.expect("Accept the answers above?")
time.sleep(1)
child.sendline("Y")
child.expect("Hours per day this program will run")
time.sleep(1)
child.sendline("24")
child.expect("Daytime P-1/ECM stage 2")
time.sleep(1)
child.sendline("8")
child.expect("Nighttime P-1/ECM stage 2")
time.sleep(1)
child.sendline("8")
child.expect("Accept the answers above")
time.sleep(1)
child.sendline("Y")
child.expect("Number of workers to run")
time.sleep(1)
child.sendline("1")
child.expect("Priority ()") # () is a subpattern
time.sleep(1)
child.sendline("10")
child.expect("Type of work to get ()")
time.sleep(1)
child.sendline("100")
child.expect("CPU cores to use ()") # Change for IBMs Watson machine
time.sleep(1)
child.sendline("2")
child.expect("Use hyperthreading for trial factoring ()")
time.sleep(1)
child.sendline("Y")
child.expect("Use hyperthreading for LL, P-1, ECM ()")
time.sleep(1)
child.sendline("N")
child.expect("Accept the answers above?")
time.sleep(1)
child.sendline("Y")

'''
child.expect("\r")
time.sleep(1)
child.sendline("N")
child.expect("\r")
time.sleep(1)
child.sendline("N")
child.expect("\r")
time.sleep(1)
child.sendline("0") # Output debug info to prime.log (o=none, 1=some, 2=lots) (0):
child.expect("\r")
#child.sendline("\n")
time.sleep(1)
child.sendline("Y") # Accept the answers above? (Y):
child.expect("\r")
#child.expect("\r")
#child.expect("\n")
time.sleep(1)
child.sendline("24")
child.expect("\n")
#child.expect("\n\r")
time.sleep(1)
#child.sendline("\r")

child.sendline("8")
child.expect("\r")
child.expect("\r")
child.expect("\r")
#child.expect("\r")
'''
child.expect("Nighttime P-1/ECM stage 2 memory in MB")
child.sendline("8")
'''
child.expect("\r")
child.expect("\n")
child.expect("\r")
child.expect("\r")
child.expect("\r")
child.expect("\r")
child.expect("\r")
child.expect("\r")
child.expect("\r")
child.expect("\n")
#child.read()
child.sendline("Y") # Accept the answers above? (Y):
child.expect("\r")

child.expect("Number of workers to run")
child.sendline("1") # Numbe
child.expect("\r")

child.expect("Type of work to get")
'''


# NOTE -- stopped here. FIXME -- the output is skipped for some reason...
'''
child.sendline("Y") # Accept the answers above? (Y):
child.expect("\r")
child.expect("\r")
child.expect("\n")
#child.expect("Accept the answers above? (Y):")
#child.expect('\w+\r\n')
#child.expect("\r")
time.sleep(1)
child.sendline("y")
'''

#Hours per day this program will run (24)
#child.expect("\n")
#child.expect("\r")

#child.expect("Type of work to get (0):", timeout=10) ## --- this marks where I broke the original expect {}
#child.expect("Optional computer name: Computer uses a dial-up connection to the Internet (N):")
#time.sleep(1)
#child.expect("Type of work to get", timeout=4) ## --- this marks where I broke the original expect {}
#time.sleep(1)
#child.sendline(os.environ["TYPE"])

'''
# This is for Watson
#child.expect("Number of workers to run")
#print(child.before)
#time.sleep(1)
#child.sendline("1\r")

# This is for Watson
#child.expect("CPU cores to use (multithreading) ")
#print(child.before)
#time.sleep(1)
#child.sendline("56\r")
'''

#child.expect("Your choice:\nUse the following values to select a work type:\n*: 1\n (*):")
'''
child.expect("Your choice:")
time.sleep(1)
child.sendline("\r")
child.expect("Done communicating with server.")
child.sendline("\x03")
time.sleep(10)
child.expect("Choose Test/Continue to restart.")
time.sleep(1)
child.sendline("5\r")
child.expect(pexpect.EOF, timeout=None) # copied from: https://stackoverflow.com/questions/11160504/simplest-way-to-run-an-expect-script-from-python
'''
#print(child.before)
#cmd_show_data = child.before
#cmd_output = cmd_show_data.split('\r\n')
#for data in cmd_output:
#    print(data)