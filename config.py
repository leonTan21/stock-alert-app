import os
from dotenv import load_dotenv

load_dotenv()

# Stock and News API keys
S_API_KEY = os.getenv("STOCK_API_KEY")
N_API_KEY = os.getenv("NEWS_API_KEY")

# Twilio credentials
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
FROM_NUMBER = os.getenv("VIRTUAL_TWILIO_NUMBER")
TO_NUMBER = os.getenv("VERIFIED_NUMBER")

# Stock and company info
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

# API endpoints
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
