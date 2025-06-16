from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime, timedelta
import io
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

app = FastAPI()

# テンプレートと静的ファイル設定
app.mount("/static", StaticFiles(directory="ui/static"), name="static")
templates = Jinja2Templates(directory="ui/templates")

@app.get("/", response_class=Response)
async def root(request: Request):
    # index.htmlにレンダリング
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/chart.png")
async def chart_png():
    # ダミーデータ作成（1日分1分足）
    now = datetime.utcnow().replace(second=0, microsecond=0)
    times = [now - timedelta(minutes=i) for i in range(60*24)]
    times.reverse()
    price = 10000 + np.cumsum(np.random.randn(len(times)))

    df = pd.DataFrame({'timestamp': times, 'close': price})
    since = now - timedelta(minutes=30)
    recent = df[df['timestamp'] >= since]

    # グラフ作成
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(recent['timestamp'], recent['close'], color='blue')
    ax.set_title('30min 1min Close Price')
    ax.set_xlabel('Time')
    ax.set_ylabel('Price')
    ax.grid(True)
    fig.autofmt_xdate()

    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png', transparent=True)
    plt.close(fig)
    buf.seek(0)

    return Response(content=buf.read(), media_type="image/png")
