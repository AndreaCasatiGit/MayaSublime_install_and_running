#********************************************************************
# content = open/close python socket port to communicate
# with the maya session you are running
#
#
# how to = backdoor(openPort=True) / backdoor(closePort=True)
# dependencies = sys, cmds
#
# author = Andrea Casati <andrea.casati@live.it>
#********************************************************************

import sys
from maya import cmds

def backdoor(openPort=False, closePort=False):
    # define the port to open
    mel_port = ':7001'
    py_port = ':7002'

    if openPort==True:
        # query if the ports are already open
        # if yes, close it and reopen it with the proper scope
        if cmds.commandPort(py_port, query=True) == True and cmds.commandPort(mel_port, query=True) == True:
            cmds.commandPort(name=py_port, close=True)
            cmds.commandPort(name=mel_port, close=True)
            cmds.commandPort(name=py_port, sourceType="python")
            cmds.commandPort(name=mel_port, sourceType="mel")
            sys.stdout.write('\nOpen two backdoors -> port %s and %s' % (mel_port, py_port))
        else:
            cmds.commandPort(name=py_port, sourceType="python")
            cmds.commandPort(name=mel_port, sourceType="mel")
            sys.stdout.write('\nOpen two backdoors -> port %s and %s' % (mel_port, py_port))

    elif closePort==True:
        if cmds.commandPort(py_port, query=True) == True and cmds.commandPort(mel_port, query=True) == True:
            cmds.commandPort(name=py_port, close=True)
            cmds.commandPort(name=mel_port, close=True)
            sys.stdout.write('\nBackdoor "%s" and "%s" closed!' % (py_port, mel_port))
        else:
            sys.stdout.write('\nNo backdoors "%s" and "%s" exists!' % (py_port, mel_port))
