import os
import subprocess
sudoPassword = '882828'
command = 'apt update'
os.popen("sudo -S %s"%(command), 'w').write('882828\n')