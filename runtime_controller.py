# runtime_controller.py

import asyncio
from ws_manager import start_stream, stop_stream

is_running = False

async def start_ws():
    global is_running
    if not is_running:
        asyncio.create_task(start_stream())
        is_running = True

async def stop_ws():
    global is_running
    if is_running:
        await stop_stream()
        is_running = False

async def get_status():
    return {"running": is_running}
