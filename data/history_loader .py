# data/history_loader.py

import pandas as pd
from datetime import datetime, timedelta
import numpy as np

def load_1min_data() -> pd.DataFrame:
    """
    過去1日分の1分足データを取得（ここではダミーデータ生成）
    実際はCSVやDBからロードしてください
    """

    now = datetime.utcnow().replace(second=0, microsecond=0)
    times = [now - timedelta(minutes=i) for i in range(60*24)]
    times.reverse()

    price = 10000 + np.cumsum(np.random.randn(len(times)))  # 適当な価格データ生成
    df = pd.DataFrame({
        'timestamp': times,
        'open': price,
        'high': price + np.random.rand(len(times)),
        'low': price - np.random.rand(len(times)),
        'close': price + np.random.randn(len(times)) * 0.5,
    })
    return df
