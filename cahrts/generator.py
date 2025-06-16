# charts/generator.py

import io
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def generate_1min_chart(data: pd.DataFrame) -> bytes:
    """
    data: DataFrameに 'timestamp', 'open', 'high', 'low', 'close' 列がある前提
    最新30分分のローソク足チャートを生成しPNGバイナリで返す
    """

    # 最新30分のデータ抽出（timestampはdatetime型想定）
    now = datetime.utcnow()
    since = now - timedelta(minutes=30)
    recent = data[data['timestamp'] >= since]

    if recent.empty:
        # データない場合は空画像
        fig, ax = plt.subplots(figsize=(4, 2))
        ax.text(0.5, 0.5, "No Data", ha='center', va='center')
    else:
        fig, ax = plt.subplots(figsize=(6, 3))
        ax.plot(recent['timestamp'], recent['close'], label='Close')
        ax.set_title('30min 1min Candlestick (Close)')
        ax.set_xlabel('Time')
        ax.set_ylabel('Price')
        ax.grid(True)

    # 画像バッファに保存
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    return buf.read()
