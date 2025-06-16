@echo off
REM uvicorn.pidファイルがあれば削除（もしあれば）
if exist uvicorn.pid del uvicorn.pid

REM uvicornをバックグラウンド起動しログをuvicorn.logに出力
start "" /b python -m uvicorn main:app --host 127.0.0.1 --port 8000 > uvicorn.log 2>&1

REM サーバ起動待ち（5秒）
timeout /t 5 > nul

echo [INFO] uvicorn started
echo [INFO] logs in uvicorn.log

REM デフォルトブラウザで起動ページを開く
start "" http://127.0.0.1:8000
