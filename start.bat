@echo off
echo [INFO] FastAPI サーバーを起動しています...
start "" cmd /c "python -m uvicorn main:app --host 127.0.0.1 --port 8000"

timeout /t 3 >nul
start "" http://127.0.0.1:8000
