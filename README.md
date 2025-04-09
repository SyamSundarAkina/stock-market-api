# Stock Market API

A Flask-based REST API that provides stock market data and analytics using the Yahoo Finance API.

## Features

- Company Information
- Real-time Stock Market Data
- Historical Market Data
- Analytical Insights with Technical Indicators

## Prerequisites

- Python 3.8+
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/stock-market-api.git
cd stock-market-api
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask server:
```bash
python app.py
```

2. Access the API endpoints:

### Endpoints

1. **Root Endpoint**
```bash
GET http://127.0.0.1:5000/
```

2. **Company Information**
```bash
GET http://127.0.0.1:5000/company_info?symbol=AAPL
```

3. **Stock Market Data**
```bash
GET http://127.0.0.1:5000/stock_market_data?symbol=AAPL
```

4. **Historical Market Data**
```bash
POST http://127.0.0.1:5000/historical_market_data
Content-Type: application/json

{
    "symbol": "AAPL",
    "start_date": "2023-01-01",
    "end_date": "2023-12-31"
}
```

5. **Analytical Insights**
```bash
POST http://127.0.0.1:5000/analytical_insights
Content-Type: application/json

{
    "symbol": "AAPL",
    "start_date": "2023-01-01",
    "end_date": "2023-12-31"
}
```

## API Response Examples

### Company Information
```json
{
    "full_name": "Apple Inc.",
    "business_summary": "...",
    "industry": "Consumer Electronics",
    "sector": "Technology"
}
```

### Analytical Insights
```json
{
    "average_price": 150.25,
    "highest_price": 160.0,
    "lowest_price": 140.0,
    "volatility": 5.25,
    "20_day_sma": 151.0,
    "trend": "Uptrend"
}
```

## Error Handling

The API returns appropriate HTTP status codes:
- 200: Successful request
- 400: Bad request (missing parameters)
- 500: Server error

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details
