:start
tasklist /FI "IMAGENAME eq Calculator.exe" 2>NUL | find /I /N "Calculator.exe">NUL
if "%ERRORLEVEL%"=="0" (
    echo Calculator is running
    start python C:\Users\enman\documents\repos\PFAlgoMaliciosos\calc.py
) else (
    echo Calculator is not running
    timeout /t 5
    goto start
)