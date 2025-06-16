# ws_manager.py

import asyncio

async def start_stream():
    print("[WS] start_stream() called")
    while True:
        await asyncio.sleep(1)
        print("[WS] Streaming...")  # 実際にはWebSocketからデータ取得など

async def stop_stream():
    print("[WS] stop_stream() called")
    # 実装するなら、ここで停止用のフラグやキャンセル処理を入れる
