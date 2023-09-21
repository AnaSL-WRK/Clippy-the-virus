Set oShellApp= WScript.CreateObject("Shell.Application")
Set oRecycleBin= oShellApp.Namespace(15)

ans = MsgBox("Do you wish to sacrifice your trash bin to Clippy?", vbYesNo + vbQuestion, "")

If ans = vbYes Then
    ' Call the EmptyRecycler subroutine
    oRecycleBin.InvokeVerb "Empty Recycle &Bin"
Else
    For i = 1 To 10
        ans = MsgBox("Do you wish to sacrifice your trash bin to Clippy?", vbYesNo + vbQuestion, "")

        If ans = vbYes Then
            oRecycleBin.InvokeVerb "Empty Recycle &Bin"
            Exit For
        End If
    Next
End If

' Subroutine to empty the Recycle Bin

    

