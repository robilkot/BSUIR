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

REM (USE FOR DEBUG) set maxnumber=6 

set /A evencheck=%maxnumber%/2*2

if %evencheck%==%maxnumber% (goto :CASE_%maxnumber%) else (echo Hello && pause && exit)

:CASE_2
	set filename=two
	goto CASE_END
:CASE_4
	set filename=four
	goto CASE_END
:CASE_6
	set filename=six
	goto CASE_END
:CASE_8
	set filename=eight
	goto CASE_END
:CASE_0
	set filename=zero
	goto CASE_END
:CASE_END
	break>%filename%.txt
	if exist %filename%.txt (echo File "%filename%" created) else (echo Error creating file)
	pause
	exit
	
