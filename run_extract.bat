@echo off
set LOGFILE="A:\APL_App\log\log_apl_auto_daily.txt"
call :LOG > %LOGFILE%
exit /B
:LOG
echo start %date% %time%
set locate="A:\APL_App"
set run_script=report_apl_auto_daily.py
cd %locate%
python %run_script%
echo finished %date% %time%
exit
