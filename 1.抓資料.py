import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

try:
    page = 1
    page_end=41125#設定結尾
    # 網址
    while True:
        url = "http://www.taipeimarathon.org.tw/survey/grade_detail.aspx?id=%d"%page
       
        # 向網頁發送 GET 請求
        response = requests.get(url)
        response.encoding = 'utf-8'
        
        # 解析網頁的HTML內容
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 在網頁上找到表格
        table = soup.find(id="BodyTextHolder_GridView1")
        if table is None :#如果是空的
                print("第%d空白"%page)
                if page <= page_end:#設定下載數
                    page += 1                
                    continue
                else:
                    print("下載完畢")
                    break
        
        #手動輸入表頭
        headers = ['次數','賽事日期','賽事名稱','成績','名次','超馬','備註','審核','證書','相片']
        
        # 提取表rows
        rows = []
        for row in table.find_all('tr')[:]:
            cells = row.find_all('td')
            row_data = [cell.text.strip() for cell in cells]
            rows.append(row_data)
        
            
        # Create a DataFrame
        df = pd.DataFrame(data=rows)
        if df.empty:#如果是空的
                print("第%d空白"%page)
                if page <= page_end:#設定下載數
                    page += 1                
                    continue
                else:
                    print("下載完畢")
                    break
        else:
                #---整理
                df = df.drop(0,axis=1)#刪第一欄空白
                df = df.drop(0,axis=0)#刪第一列數字
                df.columns = headers#加標頭
                
                
                # Save the DataFrame to a CSV file
                new_file_path ="id%d.csv"%page
               
                df.to_csv(new_file_path, index=False)
                
                print("資料已儲存%d"%page)
                try:
                    # csv檔下載完畢後等待2秒
                    time.sleep(2)
                    
                    if page <= page_end:#設定下載數
                        page += 1                
                        continue
                    else:
                        print("下載完畢")
                        break
                
                except Exception as e:
                    print("下載失敗：", e)  
                 
            
            
except Exception as e:
    print("第%d爬取失敗："%page, e)

            
