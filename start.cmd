@echo off
:loop
python punkterechner.py
choice /c YN /n /m "Willst du beenden? (Y/N)"

rem Prüfen der errorlevel, von höchstem nach niedrigstem
if errorlevel 2 (
    cls&&goto loop
) else if errorlevel 1 (
    exit
)

