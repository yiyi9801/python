import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("2014月份賽事.csv",index_col=0)

fig, ax = plt.subplots(figsize=(10, 6))
# fig, ax = plt.subplots()
plt.rcParams["font.family"] = "Microsoft JhengHei"



#畫圖
bars = data.plot(kind='bar', ax=ax)

# 圖的標籤
ax.set_title('統計2014年場次')
ax.set_xlabel('')
ax.set_ylabel('總\n數',rotation = 0,x=-1,y=-0.1)

# 圖上加數字
for bar in bars.patches:
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f'{int(bar.get_height())}',
        ha='center',
        va='bottom'
    )

# 调整布局以避免标签重叠
plt.xticks(rotation=0)
plt.tight_layout()

# 显示图表
plt.show()


