@echo off
chcp 65001 > nul
echo [INFO] GitHub へファイルをアップロードします...

REM ▼ 安全ディレクトリとして登録（1回だけでOK）
git config --global --add safe.directory C:/NAmodel

REM ▼ 変更をステージに追加
git add .
IF %ERRORLEVEL% EQU 0 (
    echo [OK] 変更をステージに追加しました。
) ELSE (
    echo [WARN] git add に失敗しました。
)

REM ▼ コミットする変更があるか確認
git diff --cached --quiet
IF %ERRORLEVEL% EQU 0 (
    echo [WARN] コミットする変更がありません。
) ELSE (
    git commit -m "自動コミット"
)

REM ▼ プッシュ実行
git push origin master
IF %ERRORLEVEL% EQU 0 (
    echo [DONE] GitHub へのプッシュが完了しました。
) ELSE (
    echo [ERROR] プッシュに失敗しました。認証情報やネット接続をご確認ください。
)

pause
