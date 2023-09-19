Dim oPlayer
Dim value
Set oPlayer = CreateObject("WMPlayer.OCX")


' Play audio
oPlayer.URL = "assets/hello.mp3"
oPlayer.controls.play 
While oPlayer.playState <> 1 ' 1 = Stopped
  WScript.Sleep 100
Wend

WScript.Sleep 700


for value = 0 to 7
  oPlayer.URL = "assets/recycle.mp3"
  oPlayer.controls.play 
  WScript.Sleep 1000
next


for value = 0 to 7
  oPlayer.URL = "assets/recycle2.mp3"
  oPlayer.controls.play 
  WScript.Sleep 1000
next



for value = 0 to 7
  oPlayer.URL = "assets/recycle3.mp3"
  oPlayer.controls.play 
  WScript.Sleep 1000
next


for value = 0 to 7
  oPlayer.URL = "assets/recycle4.mp3"
  oPlayer.controls.play 
  WScript.Sleep 1000
next


while True
  oPlayer.URL = "assets/recycle5.mp3"
  oPlayer.controls.play 
  WScript.Sleep 1000
wend

' Release the audio file
oPlayer.close
WScript.Quit