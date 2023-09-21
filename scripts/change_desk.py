import struct
import ctypes
import os, sys
from time import sleep



# DESKTOP CHANGE

SPI_SETDESKWALLPAPER = 20


simp_path1 = '../assets/clippy.png'
abs_path1 = os.path.abspath(simp_path1)

simp_path2 = '../assets/clippy2.png'
abs_path2 = os.path.abspath(simp_path2)


simp_path3 = '../assets/clippy3.png'
abs_path3 = os.path.abspath(simp_path3)


simp_path4 = '../assets/clippy4.png'
abs_path4 = os.path.abspath(simp_path4)


simp_path5 = '../assets/clippy5.png'
abs_path5 = os.path.abspath(simp_path5)


simp_path6 = '../assets/clippy6.png'
abs_path6 = os.path.abspath(simp_path6)

WALLPAPER_PATH1 = abs_path1
WALLPAPER_PATH2 = abs_path2

WALLPAPER_PATH3 = abs_path3
WALLPAPER_PATH4 = abs_path4

WALLPAPER_PATH5 = abs_path5
WALLPAPER_PATH6 = abs_path6


def is_64_windows():
    """Find out how many bits is OS. """
    return struct.calcsize('P') * 8 == 64


def get_sys_parameters_info():
    """Based on if this is 32bit or 64bit returns correct version of SystemParametersInfo function. """
    return ctypes.windll.user32.SystemParametersInfoW if is_64_windows() \
        else ctypes.windll.user32.SystemParametersInfoA


def main(arg):
    sys_parameters_info = get_sys_parameters_info()
    
    if arg == 1:
        r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH1, 3)
    
    if arg == 2:
        r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH2, 3)
    
    if arg == 3:
        r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH3, 3)
        
    if arg == 4:
        r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH4, 3)
        
    if arg == 5:
        r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH5, 3)
        
    if arg == 6:
        r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH6, 3)
        
        
        #sleep(0.1)
        #r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH2, 3)


if __name__ == "__main__":
    arg = int(sys.argv[1])
    main(arg)



