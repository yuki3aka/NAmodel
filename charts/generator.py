# charts/generator.py

import matplotlib.pyplot as plt
import os
import pandas as pd
from datetime import datetime, timedelta

CACHE_FILE = "data/last_chart.png"
CACHE_TIMESTAMP = "data/last_generated.txt"

def load_minute_data():
    # 仮の1分足データ生成（実際にはデータソースから取得）
    now = datetime.now().replace(second=0, microsecond=0)
    timestamps = [now - timedelta(minutes=i) for i in range(30)][::-1]
    prices = [30000 + i * 10 for i in range(30)]
    return pd.DataFrame({"timestamp": timestamps, "close": prices})

def generate_chart():
    now = datetime.now()

    # 直近の生成から1分未満ならキャッシュを使う
    if os.path.exists(CACHE_FILE) and os.path.exists(CACHE_TIMESTAMP):
        with open(CACHE_TIMESTAMP, "r") as f:
            ts = datetime.fromisoformat(f.read().strip())
            if now - ts < timedelta(seconds=60):
                return CACHE_FILE

    # データ取得
    df = load_minute_data()

    # チャート生成
    plt.figure(figsize=(10, 8))  # 高さ2倍
    plt.plot(df["timestamp"], df["close"], label="Close Price")
    plt.title("▶1分足チャート (BTC-USD)", fontproperties="MS Gothic")  # 日本語対応
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    # 保存
    plt.savefig(CACHE_FILE)
    with open(CACHE_TIMESTAMP, "w") as f:
        f.write(now.isoformat())

    return CACHE_FILE
