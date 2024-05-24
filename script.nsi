
OutFile "CalculatorInstaller.exe"
InstallDir "$PROGRAMFILES\Calculator"
RequestExecutionLevel user
Section "MainSection" SEC01
SetOutPath $INSTDIR
File /r "build\exe.win-amd64-3.12*.*"
CreateShortCut "$DESKTOP\Calculator.lnk" "$INSTDIR\calculator.exe"
SectionEnd
