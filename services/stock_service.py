import config as cf
import requests
from typing import Dict, Any

class StockService:
    def __init__(self):
        # If you're using Alpha Vantage or similar
        self.api_key = cf.api_key  # Better to use environment variables
        self.base_url = "https://www.alphavantage.co"

    def get_stock_data(self, symbol: str) -> Dict[str, Any]:
        try:
            stock = yf.Ticker(symbol)
            return {
                "info": stock.info,
                "history": stock.history(period="1y").to_dict()
            }
        except Exception as e:
            raise Exception(f"Error fetching stock data: {str(e)}")

    def get_market_news_sentiment(self) -> Dict[str, Any]:
        try:
            response = requests.get(
                f"{self.base_url}",
                params={""}
                headers={"Authorization": f"Bearer {self.api_key}"}
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching market news: {str(e)}")