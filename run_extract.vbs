Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "A:\APL_App\batch\run_extract.bat" & Chr(34), 0
Set WinScriptHost = Nothing