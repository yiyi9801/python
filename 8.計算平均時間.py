import pandas as pd


df = pd.read_csv('All.csv')

# 轉換為日期
df['賽事日期'] = pd.to_datetime(df['賽事日期'])
df['年份'] = df['賽事日期'].dt.year


# 轉換為時間
df['成績'] = pd.to_timedelta(df['成績'])

# 照年分組計算平均
yearly_average_time = df.groupby('年份')['成績'].mean()

# 換成字串
yearly_average_time_str = yearly_average_time.apply(lambda x: str(x))


