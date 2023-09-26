import sys
from cx_Freeze import setup, Executable
import os.path


PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["scripts","importlib", "multiprocessing", "subprocess", "time", "os","pynput","pygetwindow", "struct","ctypes","sys","tkinter","random"], 
                    "zip_include_packages": ["assets", "scripts"],
                    "include_files" : [os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'), os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll')]}

base="Win32GUI" #should be used only for Windows GUI app

if sys.platform == "win32":
    base = "Win32GUI"
setup(
    name="Clipboard",
    version="0.1",
    description="Clippy!",
    options={"build_exe": build_exe_options},
    executables=[Executable("runner.py", base=base)],
)