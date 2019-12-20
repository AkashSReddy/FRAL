import os
import subprocess
from face import authenticate

while(True):
    s = str(input()) 
    if 'sudo' in s:
        command = s.replace('sudo', '').lstrip()
        if(authenticate() == 'Hritik'):
            os.popen("sudo -S %s"%("apt update"), 'w').write('882828\n')
        else:
            print("You are not the sudo user")
    else:
        process = subprocess.Popen(s.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        print(output)
