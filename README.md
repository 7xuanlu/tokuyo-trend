# Tokuyo trend
Author: Martin Lu
Date: 2018-12-21  
[Intro video](https://youtu.be/QN9nfmx8zT0)

## Introduction
tokuyo-trend 被打造成示範性的服務應用雛形。連結 Google Trend API，呈現熱點資料到企業內部網站。使用者在搜尋列輸入關鍵字，傳送到 Google Trend API，成功後回傳關鍵字資料，並視覺化成趨勢圖。

## Architecture
### Django
作為網站開發基礎框架，處理網站登入登出、網址委發、MTV(Model, Template, View)架構。
### Google Trend
API 資料來源，由於 Google Trend API 在開發時(2018 年底)關閉服務，只能由第三方套件 pytrends 向 Google Trend 索取資料，與 Google Trend 的資料相比有些許誤差。
### Chart.js
取得 Google Trend 資料後，將資料視覺化，呈現時間趨勢圖，代表這個關鍵字在不同時間段，相對的熱度(根據搜尋引擎接受 query 時計算)

## Setup
First you can clone the repo
```
git clone https://github.com/h164654156465/realtime-face-detection-azure.git
```

### Create virtual environment

On Windows 
```
> python -m venv myenv
```
Or on Linux/MacOS
```
$ python3 -m venv myenv
```

### Activate your virtual environment

On Windows
```
> .\myenv\Scripts\activate
```

Or on Linux/MacOS
```
$ source env/bin/activate
```

After activating the environment, you'll see something like this:
```
(venv) > <your-path>
```

### Install your packages
```
(venv) > pip install -r requirements.txt
```

## Test the application
### Navigate the website
Open the development server and it will start to listen on http://127.0.0.1:8000/
```
(venv) > python manage.py runserver
```

Navigate to that URL, you'll see the website is up and running.

> Default login information is:  
> Account: test  
> Password: testtest123

### Leave virtual environment
If you've done navigating this website, you can deactivate the virtual environment
```
(venv) > deactivate
```