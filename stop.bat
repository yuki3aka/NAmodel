@echo off
echo [INFO] uvicorn を含むプロセスを検索して終了します...

for /f "tokens=2 delims=," %%a in ('tasklist /v /fo csv ^| findstr /i "uvicorn"') do (
    echo [INFO] プロセス ID: %%a を終了します...
    taskkill /PID %%a /F
)

echo [DONE] uvicorn プロセス停止完了。
pause
