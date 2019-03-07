# tokuyo-trend
作者: 呂佳奇  
日期: 2018-12-21  
[介紹影片 ](https://youtu.be/QN9nfmx8zT0)

## 簡介
tokuyo-trend 被打造成示範性的服務應用雛形。連結 Google Trend API，呈現熱點資料到企業內部網站。使用者在搜尋列輸入關鍵字，傳送到 Google Trend API，成功後回傳關鍵字資料，並視覺化成趨勢圖。

## 架構
### Django
作為網站開發基礎框架，處理網站登入登出、網址委發、MTV(Model, Template, View)架構。
### Google Trend
API 資料來源，由於 Google Trend API 在開發時(2018 年底)關閉服務，只能由第三方套件 pytrends 向 Google Trend 索取資料，與 Google Trend 的資料相比有些許誤差。
### Chart.js
取得 Google Trend 資料後，將資料視覺化，呈現時間趨勢圖，代表這個關鍵字在不同時間段，相對的熱度(根據搜尋引擎接受 query 時計算)
