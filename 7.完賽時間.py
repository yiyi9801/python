import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# 讀檔
file = '成績2000+.csv'
df = pd.read_csv(file)

# 年份去掉小數
df['年份'] = df['年份'].astype(int)

# 轉換時間
df['成績'] = pd.to_timedelta(df['成績'])
# 加欄位換算秒數
df['average_time_seconds'] = df['成績'].dt.total_seconds()

# 畫圖
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df['年份'], df['average_time_seconds'], marker='o', color='b',linestyle='dotted')

ax.set_title('每年的平均完賽时间')
ax.set_xlabel('年')
ax.set_ylabel('平均时间')
ax.set_ylim(16000,20000)
# 寫字
for i, row in df.iterrows():
    avg_time = row['成績']
    avg_time_str = str(avg_time).split(' ')[-1]  #取時間
    avg_time_str = avg_time_str.split('.')[0]  #去掉小數
    ax.text(
        row['年份'],
        row['average_time_seconds'],
       
        avg_time_str,
        ha='center',
        va='bottom',
        color='red'
    )

# 
ax.tick_params(axis='x', rotation=0)

# Y軸刻度
time_ticks = [
    # "00:00", "01:00", "01:30", 
    # "02:00", "02:30", "03:00","03:30", 
    "04:00", "04:30", "05:00",
    "05:30","06:00"
]

time_labels = [datetime.strptime(t, "%H:%M") for t in time_ticks]
time_seconds = [(t.hour * 3600 + t.minute * 60) for t in time_labels]

ax.set_yticks(time_seconds)
ax.set_yticklabels(time_ticks)


plt.tight_layout()

plt.show()


