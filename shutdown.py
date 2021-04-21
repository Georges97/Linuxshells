#Testing linux commands in python
import os


def poweroff():
    os.system('sudo shutdown now')


poweroff()