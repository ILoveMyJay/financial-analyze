# Stock Analysis Application

## Project Overview

This is a simple stock analysis application that allows users to view K-line charts for stocks and see if they match a specific trading strategy.

## Technology Stack

### Backend

*   **Framework:** FastAPI
*   **Language:** Python
*   **Data Source:** Ashare (via a custom module)

### Frontend

*   **Framework:** Vue.js
*   **Language:** JavaScript
*   **Charting Library:** ECharts
*   **HTTP Client:** Axios

## Business Logic

The application includes a highlighting strategy to identify stocks that may be of interest. A stock is highlighted if it meets the following criteria:

1.  **Low Price Volatility:** The price change over the last 15 days is less than 10% of the average price during that period.
2.  **Volume Reduction:** The average trading volume over the last 15 days is lower than the average volume of the 15 days prior to that.

## How to Run the Project

### Backend

1.  Navigate to the `backend` directory:
    ```bash
    cd backend
    ```
2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Start the FastAPI server:
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```
    The backend server will be running at `http://localhost:8000`.

### Frontend

1.  Navigate to the `frontend/stock-app` directory:
    ```bash
    cd frontend/stock-app
    ```
2.  Install the required dependencies:
    ```bash
    npm install
    ```
3.  Start the Vue.js development server:
    ```bash
    npm run serve
    ```
    The frontend application will be available at `http://localhost:8080` (or another port if 8080 is in use).
