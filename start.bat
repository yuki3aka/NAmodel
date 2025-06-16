@echo off
REM Delete previous PID file if exists
if exist uvicorn.pid del uvicorn.pid

REM Start uvicorn in new window, redirect logs
start "" python -m uvicorn main:app --host 127.0.0.1 --port 8000 > uvicorn.log 2>&1

REM Wait a bit for uvicorn to start
timeout /t 5 > nul

REM Get PID of the python.exe running uvicorn and save it
for /f "tokens=2 delims=," %%a in ('tasklist /fi "imagename eq python.exe" /v /fo csv ^| findstr uvicorn') do (
    echo %%~a > uvicorn.pid
    goto done
)

:done
echo [INFO] uvicorn started, PID saved in uvicorn.pid
echo [INFO] logs in uvicorn.log

REM Open browser
start "" http://127.0.0.1:8000
