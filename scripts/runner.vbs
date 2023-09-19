set shell = createobject("wscript.shell")
count = 0
do until count = 5
shell.run("""popup.vbs""")
count = count +1
WScript.Sleep 1000
loop