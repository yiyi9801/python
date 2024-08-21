import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('統計每年場次2000-.csv',index_col=0)
df2 = pd.read_csv('統計每年場次2000+.csv',index_col=0)
df3 = pd.read_csv('統計每年記錄2000-.csv',index_col=0)
df4 = pd.read_csv('統計每年記錄2000+.csv',index_col=0)


plt.rcParams["font.family"] = "Microsoft JhengHei"
fig, ax = plt.subplots(2, 2, figsize=(18, 10))

#畫第1張圖
bars = df1.plot(kind='bar', ax=ax[0,0],color='b')

# 圖的標籤
ax[0,0].set_title('統計2000年前場次')
ax[0,0].set_xlabel('年')
ax[0,0].set_ylabel('總\n數',rotation = 0,x=-1,y=-0.1)
ax[0,0].tick_params(axis='x', rotation=45)
# 圖上加數字
for bar in bars.patches:
    ax[0,0].text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f'{int(bar.get_height())}',
        ha='center',
        va='bottom'
    )

#畫第2張圖
bars2 = df2.plot(kind='bar', ax=ax[0,1],color='g')

# 圖的標籤
ax[0,1].set_title('統計2000年後場次')
ax[0,1].set_xlabel('年')
ax[0,1].set_ylabel('總\n數',rotation = 0,x=-1,y=-0.1)
ax[0,1].tick_params(axis='x', rotation=45)
# 圖上加數字
for bar in bars2.patches:
    ax[0,1].text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f'{int(bar.get_height())}',
        ha='center',
        va='bottom'
    )

#畫第3張圖
bars3 = df3.plot(kind='bar', ax=ax[1,0],color='b')

# 圖的標籤
ax[1,0].set_title('統計2000年前紀錄')
ax[1,0].set_xlabel('年')
ax[1,0].set_ylabel('總\n數',rotation = 0,x=-1,y=-0.1)
ax[1,0].tick_params(axis='x', rotation=45)
# 圖上加數字
for bar in bars3.patches:
    ax[1,0].text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f'{int(bar.get_height())}',
        ha='center',
        va='bottom'
    )

#畫第4張圖
bars4 = df4.plot(kind='bar', ax=ax[1,1],color='g')

# 圖的標籤
ax[1,1].set_title('統計2000年後紀錄')
ax[1,1].set_xlabel('年')
ax[1,1].set_ylabel('總\n數',rotation = 0,x=-1,y=-0.1)
ax[1,1].tick_params(axis='x', rotation=45)
# 圖上加數字
for bar in bars4.patches:
    ax[1,1].text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f'{int(bar.get_height())}',
        ha='center',
        va='bottom'
    )
# 调整布局以避免标签重叠

plt.tight_layout()

# 显示图表
plt.show()


