from config import (
    S_API_KEY,
    N_API_KEY,
    STOCK_NAME,
    COMPANY_NAME,
    STOCK_ENDPOINT,
    NEWS_ENDPOINT,
    TWILIO_SID,
    TWILIO_AUTH_TOKEN,
    TO_NUMBER,
    FROM_NUMBER,
)
import requests
from twilio.rest import Client

# ---------------- STEP 1: Get stock prices ----------------

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": S_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

# Yesterday's closing price
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])
print(f"Yesterday's closing price: {yesterday_closing_price}")

# Day before yesterday's closing price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])
print(f"Day before yesterday's closing price: {day_before_yesterday_closing_price}")

# Difference and up/down
difference = yesterday_closing_price - day_before_yesterday_closing_price
up_down = "🔺" if difference > 0 else "🔻"

# Percentage difference
diff_percent = round((difference / yesterday_closing_price) * 100)
print(f"Percentage change: {diff_percent}%")

# ---------------- STEP 2: Get News if change > threshold ----------------

THRESHOLD = 5  # percent

if abs(diff_percent) > THRESHOLD:
    news_params = {
        "apiKey": N_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json().get("articles", [])

    # First 3 articles
    three_articles = articles[:3]

    # Format articles
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}\nBrief: {article['description']}"
        for article in three_articles
    ]
    print(formatted_articles)

    # ---------------- STEP 3: Send via Twilio ----------------
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=FROM_NUMBER,
            to=TO_NUMBER
        )
        print(f"Message sent: SID {message.sid}")
