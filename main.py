from config import API_KEY, STOCK_NAME, COMPANY_NAME, STOCK_ENDPOINT, NEWS_ENDPOINT
import requests

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey" : API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
diff_percent = (difference / float(yesterday_closing_price)) * 100

## if diff_percentage > 4, send alert
# if diff_percent > 4:
#     return null