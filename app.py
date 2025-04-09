# Import necessary libraries
from flask import Flask, request, jsonify  # Flask for API, request for handling POST, jsonify for JSON responses
import yfinance as yf  # Yahoo Finance API to fetch company and stock data
from datetime import datetime  # For handling dates
import pandas as pd  # For data manipulation and analysis
import numpy as np  # For numerical operations

# Initialize Flask app
app = Flask(__name__)

# Root URL
@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Flask API!'}), 200

# Favicon handler
@app.route('/favicon.ico')
def favicon():
    return '', 204  # Return an empty response with a 204 No Content status

# 1. Company Information Endpoint
@app.route('/company_info', methods=['GET'])
def get_company_info():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({'error': 'Company symbol is required'}), 400
    try:
        company = yf.Ticker(symbol)
        info = company.info
        company_data = {
            'full_name': info.get('longName', 'N/A'),
            'business_summary': info.get('longBusinessSummary', 'N/A'),
            'industry': info.get('industry', 'N/A'),
            'sector': info.get('sector', 'N/A'),
            'key_officers': info.get('companyOfficers', 'N/A')
        }
        return jsonify(company_data), 200
    except Exception as e:
        return jsonify({'error': f'Failed to fetch company info: {str(e)}'}), 500

# 2. Stock Market Data Endpoint
@app.route('/stock_market_data', methods=['GET'])
def get_stock_market_data():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({'error': 'Company symbol is required'}), 400
    try:
        stock = yf.Ticker(symbol)
        info = stock.info
        stock_data = {
            'market_state': info.get('marketState', 'N/A'),
            'current_price': info.get('regularMarketPrice', info.get('currentPrice', 'N/A')),
            'price_change': info.get('regularMarketChange', 'N/A'),
            'percent_change': info.get('regularMarketChangePercent', 'N/A'),
            'volume': info.get('regularMarketVolume', 'N/A'),
            'market_cap': info.get('marketCap', 'N/A')
        }
        return jsonify(stock_data), 200
    except Exception as e:
        return jsonify({'error': f'Failed to fetch stock market data: {str(e)}'}), 500

# 3. Historical Market Data Endpoint
@app.route('/historical_market_data', methods=['POST'])
def get_historical_market_data():
    data = request.get_json()
    if not data or 'symbol' not in data or 'start_date' not in data or 'end_date' not in data:
        return jsonify({'error': 'Symbol, start_date, and end_date are required'}), 400
    symbol = data['symbol']
    start_date = data['start_date']
    end_date = data['end_date']
    try:
        stock = yf.Ticker(symbol)
        history = stock.history(start=start_date, end=end_date)
        history_data = history.reset_index().to_dict(orient='records')
        return jsonify(history_data), 200
    except Exception as e:
        return jsonify({'error': f'Failed to fetch historical data: {str(e)}'}), 500

# 4. Analytical Insights Endpoint
@app.route('/analytical_insights', methods=['POST'])
def get_analytical_insights():
    data = request.get_json()
    if not data or 'symbol' not in data or 'start_date' not in data or 'end_date' not in data:
        return jsonify({'error': 'Symbol, start_date, and end_date are required'}), 400
    symbol = data['symbol']
    start_date = data['start_date']
    end_date = data['end_date']
    try:
        stock = yf.Ticker(symbol)
        history = stock.history(start=start_date, end=end_date)
        avg_price = history['Close'].mean()
        max_price = history['Close'].max()
        min_price = history['Close'].min()
        volatility = history['Close'].std()
        sma_20 = history['Close'].rolling(window=20).mean().iloc[-1] if len(history) >= 20 else None
        insights = {
            'average_price': round(avg_price, 2),
            'highest_price': round(max_price, 2),
            'lowest_price': round(min_price, 2),
            'volatility': round(volatility, 2),
            '20_day_sma': round(sma_20, 2) if sma_20 else 'N/A',
            'trend': 'Uptrend' if sma_20 and history['Close'].iloc[-1] > sma_20 else 'Downtrend' if sma_20 else 'N/A'
        }
        return jsonify(insights), 200
    except Exception as e:
        return jsonify({'error': f'Failed to fetch analytical insights: {str(e)}'}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)



'''# PowerShell
curl "http://127.0.0.1:5000/"

# Command Prompt
curl -X GET "http://127.0.0.1:5000/"

# PowerShell
curl "http://127.0.0.1:5000/company_info?symbol=AAPL"

# Command Prompt
curl -X GET "http://127.0.0.1:5000/company_info?symbol=AAPL"

# PowerShell
curl "http://127.0.0.1:5000/stock_market_data?symbol=AAPL"

# Command Prompt
curl -X GET "http://127.0.0.1:5000/stock_market_data?symbol=AAPL"

# PowerShell
$body = @{
    symbol='AAPL'
    start_date='2023-01-01'
    end_date='2023-12-31'
} | ConvertTo-Json

curl -Method POST `
     -ContentType 'application/json' `
     -Body $body `
     "http://127.0.0.1:5000/historical_market_data"

# Command Prompt
curl -X POST ^
     -H "Content-Type: application/json" ^
     -d "{\"symbol\":\"AAPL\",\"start_date\":\"2023-01-01\",\"end_date\":\"2023-12-31\"}" ^
     "http://127.0.0.1:5000/historical_market_data"
     
# PowerShell
$body = @{
    symbol='AAPL'
    start_date='2023-01-01'
    end_date='2023-12-31'
} | ConvertTo-Json

curl -Method POST `
     -ContentType 'application/json' `
     -Body $body `
     "http://127.0.0.1:5000/analytical_insights"

# Command Prompt
curl -X POST ^
     -H "Content-Type: application/json" ^
     -d "{\"symbol\":\"AAPL\",\"start_date\":\"2023-01-01\",\"end_date\":\"2023-12-31\"}" ^
     "http://127.0.0.1:5000/analytical_insights"
     
     '''  