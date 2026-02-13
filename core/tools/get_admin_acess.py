import elevate
import ctypes
import platform
import os

def check_admin(sed_request:bool):
    if platform.system().lower() == 'windows':
        if sed_request:
            if ctypes.windll.shell32.IsUserAnAdmin():
                return True
            else:
                try:
                    elevate.elevate(graphical=True)
                    if ctypes.windll.shell32.IsUserAnAdmin():
                        return True
                    else:
                        return False
                except:
                    return 'process intrupted'
        else:
            return ctypes.windll.shell32.IsUserAnAdmin()
    elif platform.system() == 'Linux':
        if os.popen('whoami') != 'root':
            elevate.elevate(graphical=True)
