import pandas as pd

pd_data=pd.DataFrame()

i=1
i_end=41125
while True:
    try:
        data = pd.read_csv("id%d.csv"%i)
            
        pd_data = pd.concat([pd_data,data])
        if i <= i_end:#設定數
            i += 1
            print("%d完畢"%i)
            continue
        
        else:
            print("完畢")
            break
    except FileNotFoundError:
        i += 1                
        pass
pd_data.to_csv("All.csv")