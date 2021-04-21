#Testing linux commands in python
import os
import subprocess

def poweroff():
    os.system('sudo shutdown now')


poweroff()