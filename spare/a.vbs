
dim filesys
Set filesys = CreateObject("Scripting.FileSystemObject")
If filesys.FileExists("clippy.jpg") Then
   MsgBox "File created."
End If
