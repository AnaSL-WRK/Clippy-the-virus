' Define the path to the wallpaper image
Dim WallpaperPath


' Get the folder where the VBScript is located
Set objShell = CreateObject("WScript.Shell")
ScriptDir = objShell.CurrentDirectory

' Define the relative path to the wallpaper image


RelativePath = "\assets\clippy.png"
WallpaperPath = ScriptDir & RelativePath
objShell.Run "reg add ""HKCU\Control Panel\Desktop"" /v Wallpaper /t REG_SZ /d """ & WallpaperPath & """ /f", 0, True
objShell.Run "%windir%\System32\RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters", 1, True


RelativePath = "\assets\clippy2.png"
WallpaperPath = ScriptDir & RelativePath
objShell.Run "reg add ""HKCU\Control Panel\Desktop"" /v Wallpaper /t REG_SZ /d """ & WallpaperPath & """ /f", 0, True
objShell.Run "%windir%\System32\RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters", 1, True