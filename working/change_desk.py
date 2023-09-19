import struct
import ctypes
import os
from time import sleep



# DESKTOP CHANGE

SPI_SETDESKWALLPAPER = 20


simp_path1 = '../assets/clippy.png'
abs_path1 = os.path.abspath(simp_path1)

simp_path2 = '!CODE/bonzi.png'
abs_path2 = os.path.abspath(simp_path2)


WALLPAPER_PATH1 = abs_path1
WALLPAPER_PATH2 = abs_path2


def is_64_windows():
    """Find out how many bits is OS. """
    return struct.calcsize('P') * 8 == 64


def get_sys_parameters_info():
    """Based on if this is 32bit or 64bit returns correct version of SystemParametersInfo function. """
    return ctypes.windll.user32.SystemParametersInfoW if is_64_windows() \
        else ctypes.windll.user32.SystemParametersInfoA


def change_wallpaper():
    sys_parameters_info = get_sys_parameters_info()
    
  
    r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH1, 3)
        #sleep(0.1)
        #r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH2, 3)

    # When the SPI_SETDESKWALLPAPER flag is used,
    # SystemParametersInfo returns TRUE
    # unless there is an error (like when the specified file doesn't exist).
    if not r:
        print(ctypes.WinError())


change_wallpaper()


