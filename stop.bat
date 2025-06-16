@echo off
echo [INFO] uvicorn プロセスを停止します...

if not exist uvicorn.pid (
    echo [WARN] uvicorn.pid ファイルがありません。手動で停止してください。
    pause
    exit /b
)

set /p PID=<uvicorn.pid

taskkill /PID %PID% /F

del uvicorn.pid

echo [DONE] uvicorn を停止しました。
pause
