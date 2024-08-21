import pandas as pd


df = pd.read_csv("all.csv")

#如果賽事名稱是空白的，清除一列
# df = data.dropna(subset=['賽事名稱'])

# 馬拉松紀錄人數(所有資料筆數:19816)

# 紀錄次數(總共資料665755)

# 統計場次(登記人數最多的場次)
# value_counts = df['賽事名稱'].value_counts()
# print(value_counts)
# value_counts.to_csv("統計場次.csv")
# 每年場次 先排日期再統計
# subset_df = df[['賽事日期', '賽事名稱']]
#按照日期分組，然後統計每個賽事名稱次數
# grouped = subset_df.groupby('賽事日期')['賽事名稱'].value_counts().reset_index(name='count')
# grouped.to_csv("統計每年場次.csv")

# 已審核 未審核
# value_counts = df['審核'].value_counts()
# print(value_counts)
# 已審核    618027
# 未審核     47448
# 登錄中       280

#年份統計
df['賽事日期'] = pd.to_datetime(df['賽事日期'])
#加一個年份欄計算年份
df['年份'] = df['賽事日期'].dt.year

#分審核
# data_y =df[df['審核']=='已審核']
# data_n =df[df['審核']=='未審核']

#以年份值分組 照年份排
yearly_counts = df['年份'].value_counts().sort_index()
# yearly_counts_y = data_y['年份'].value_counts().sort_index()
# yearly_counts_n = data_n['年份'].value_counts().sort_index()

#抓2014
data_n =df[df['年份']==2014]
# data_n.to_csv('2014資料.csv')
#統計
# grouped = data_n.groupby('賽事日期')['賽事名稱'].value_counts().reset_index(name='count')
#加月份照月份排
data_n['月份'] = data_n['賽事日期'].dt.month
month_counts = data_n['月份'].value_counts().sort_index()
# month_counts.to_csv('2014月份紀錄.csv')

#每月賽事
# month_counts = grouped['月份'].value_counts().sort_index()
# month_counts.to_csv('2014月份賽事.csv')

