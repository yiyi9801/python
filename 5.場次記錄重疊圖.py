import pandas as pd
import matplotlib.pyplot as plt

# 讀取
file1 = '2014月份紀錄.csv'
file2 = '2014月份賽事.csv'

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

#匯入字型
plt.rcParams["font.family"] = "Microsoft JhengHei"
fig, ax1 = plt.subplots(figsize=(12, 6))

# 第一張圖
ax1.bar(df1['月份'], df1['記錄數'], color='b', alpha=0.3, label='記錄數')
ax1.set_xlabel('月份')
ax1.set_ylabel('記錄數', color='b')
ax1.tick_params(axis='y', labelcolor='b')
ax1.set_ylim(0,12000)#設定Y軸範圍
# 數值
for i, row in df1.iterrows():
    ax1.text(
        row['月份'],
        row['記錄數'],
        f'{row["記錄數"]:.0f}',
        ha='center',
        va='top',
        color='blue'
    )

# 第2張圖
ax2 = ax1.twinx()
ax2.plot(df2['月份'], df2['賽事數'], marker='o', color='r', label='賽事數', linestyle='dotted')
ax2.set_ylabel('賽事數', color='r')
ax2.tick_params(axis='y', labelcolor='r')
ax2.set_ylim(0,200)#設定Y軸範圍
# 數值
for i, row in df2.iterrows():
    ax2.text(
        row['月份'],
        row['賽事數'],
        f'{row["賽事數"]:.0f}',
        ha='center',
        va='bottom',
        
    )

# 设置 x 轴刻度旋转角度
ax1.tick_params(axis='x', rotation=45)

# 添加图例
fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)

# 调整布局以避免标签重叠
plt.tight_layout()

# 显示图表
plt.show()

# 如果需要，可以将图表保存到文件
# 例如：fig.savefig('yearly_combined_chart.png')
