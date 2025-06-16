function updateChart() {
  const chart = document.getElementById("chart");
  const timestamp = new Date().getTime(); // キャッシュ回避のため
  chart.src = `/chart.png?ts=${timestamp}`;
}

// 1秒ごとにチャートを更新
setInterval(updateChart, 1 * 1000);

// 初回読み込み後も即座に1回更新
window.onload = updateChart;
