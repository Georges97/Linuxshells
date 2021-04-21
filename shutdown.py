#Testing linux commands in python
import os


def poweroff():
    os.system('shutdown now')


poweroff()