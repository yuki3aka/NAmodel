@echo off
echo [INFO] uvicorn プロセスを停止します...

REM PowerShellを使ってuvicornを含むPythonプロセスを強制終了
powershell -Command "Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -match 'uvicorn' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }"

echo [DONE] uvicorn を停止しました。
pause
