from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from Ashare import get_price  # Import from Ashare.py
import logging
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Add CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/stock/{stock_code}")
def get_stock_data(stock_code: str):
    try:
        # Fetch daily k-line data using the synchronous get_price function
        df = get_price(stock_code, frequency='1d', count=30)

        if df is None or df.empty:
            return {"stock_data": [], "highlight": False, "message": "No data found for the given stock code."}

        # Highlighting logic
        highlight = False
        # Check for low price volatility in the last 15 days
        recent_df = df.tail(15)
        price_change_ratio = (recent_df['close'].max() - recent_df['close'].min()) / recent_df['close'].mean()

        # Check for volume reduction
        # Compare the average volume of the last 15 days with the 15 days before that
        if len(df) >= 30:
            previous_df = df.iloc[-30:-15]
            recent_avg_volume = recent_df['volume'].mean()
            previous_avg_volume = previous_df['volume'].mean()

            if price_change_ratio < 0.1 and recent_avg_volume < previous_avg_volume:
                highlight = True

        return {"stock_data": df.to_dict(orient='records'), "highlight": highlight}

    except Exception as e:
        logger.error(f"Error fetching stock data for {stock_code}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal Server Error")
