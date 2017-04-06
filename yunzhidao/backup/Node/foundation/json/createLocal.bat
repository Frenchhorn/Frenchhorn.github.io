@echo off
chcp 65001
echo window.localJson=[ >> temp.json
for /R %%s in (*.jpg,*.png) do (
echo ^"%%s^", >> temp.json
)
echo ] >> temp.json

SetLocal EnableDelayedExpansion
Set  File=temp.json
Set  Str=\
Set  Replace=/
Set  File=%File:"=%
For /F "Usebackq Delims=" %%i In ("%File%") Do (
    Set "Line=%%i"
    Echo !Line:%Str%=%Replace%! >> local.json
)
del temp.json