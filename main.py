import tkinter as tk
import requests
import json
from datetime import date

saved_weather_data = []

# 天気情報を取得する関数
def get_weather():
    # OpenWeatherMap APIキー
    API_KEY = "d72b205804d2ad660924862a76799f33"

    # 東京の都市ID
    CITY_ID = 1850147

    # OpenWeatherMap APIにアクセス
    url = f"http://api.openweathermap.org/data/2.5/weather?id={CITY_ID}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    print(f"API Response Code: {response.status_code}")
    print(f"API Request URL: {url}")
    print(f"API Response Data: {response.text}")


    if response.status_code == 200:
        # レスポンスデータをJSON形式で解析
        data = json.loads(response.text)
        
        # 天気情報を取得
        weather = data["weather"][0]["description"]
        
        # 今日の日付を取得
        today = date.today()
        
        # ラベルに天気情報を表示
        result_label.config(text=f"東京の天気 ({today}): {weather}")

        # 天気情報を保存
        saved_weather_data.append(f"東京の天気 ({today}): {weather}")

        # ラベルに天気情報を表示
        result_label.config(text=f"東京の天気 ({today}): {weather}")

    else:
        result_label.config(text="天気情報を取得できません")

# 天気情報を保存する関数
def save_weather():
    # 保存するファイル名を生成（日付を含む）
    today = date.today()
    filename = f"tokyo_weather_{today}.txt"
    
    # 天気情報を取得
    weather_info = result_label.cget("text")
    
    # ファイルに天気情報を保存
    with open(filename, "w") as file:
        file.write(weather_info)
    
    save_status_label.config(text=f"天気情報を{filename}に保存しました")

# 天気情報を表示するウィンドウを作成
def view_saved_weather():
    view_window = tk.Toplevel()
    view_window.title("保存された天気情報")

    # リストボックスを作成して、保存された天気情報を表示
    listbox = tk.Listbox(view_window, selectmode=tk.SINGLE)
    for item in saved_weather_data:
        listbox.insert(tk.END, item)
    listbox.pack()

# Tkinterウィンドウを作成
window = tk.Tk()
window.title("東京の天気")
window.geometry("800x600")
# 天気情報を表示するラベル
result_label = tk.Label(window, text="", font=("Helvetica", 16))
result_label.pack(pady=50)

# 天気情報を取得するボタン
get_weather_button = tk.Button(window, text="天気を取得", command=get_weather)
get_weather_button.pack()

# 天気情報を保存するボタン
save_weather_button = tk.Button(window, text="天気を保存", command=save_weather)
save_weather_button.pack()

# 保存された天気情報を表示するボタン
view_saved_button = tk.Button(window, text="保存された天気情報を表示", command=view_saved_weather)
view_saved_button.pack()

# 保存ステータスを表示するラベル
save_status_label = tk.Label(window, text="", font=("Helvetica", 12))
save_status_label.pack()


# Tkinterウィンドウを開始
window.mainloop()
