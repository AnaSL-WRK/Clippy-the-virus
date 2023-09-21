Dim oPlayer
Dim value
Set oPlayer = CreateObject("WMPlayer.OCX")

' Get the directory to the parent folder of this script
Set objFSO = CreateObject("Scripting.FileSystemObject")
currentDirectory = objFSO.GetAbsolutePathName(".")
parentDirectory = objFSO.GetParentFolderName(currentDirectory)

' Play audio
oPlayer.URL = parentDirectory & "\" & "\assets\hello.mp3"
oPlayer.controls.play 
While oPlayer.playState <> 1 ' 1 = Stopped
  WScript.Sleep 1
Wend

WScript.Sleep 100


for value = 0 to 7
  oPlayer.URL = parentDirectory & "\" & "assets\recycle.mp3"
  oPlayer.controls.play 
  WScript.Sleep 1000
next


for value = 0 to 7
  oPlayer.URL = parentDirectory & "\" & "assets\recycle2.mp3"
  oPlayer.controls.play 
  WScript.Sleep 1000
next



for value = 0 to 7
  oPlayer.URL = parentDirectory & "\" & "assets\recycle3.mp3"
  oPlayer.controls.play 
  WScript.Sleep 1000
next


for value = 0 to 7
  oPlayer.URL = parentDirectory & "\" & "assets\recycle4.mp3"
  oPlayer.controls.play 
  WScript.Sleep 1000
next


while True
  oPlayer.URL = parentDirectory & "\" & "assets\recycle5.mp3"
  oPlayer.controls.play 
  WScript.Sleep 1000
wend

' Release the audio file
oPlayer.close