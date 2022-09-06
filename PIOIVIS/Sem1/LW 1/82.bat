@echo off

setlocal enabledelayedexpansion

set nodotdate=%date:.=%
set maxnumber=0

for /l %%i in (0,1,7) do (
	set checknumber=!nodotdate:~%%i,1!
	if "!checknumber!" gtr "!maxnumber!" (
		set maxnumber=!checknumber!
	)
)

echo The max num in date is %maxnumber%
pause
