Stock Market AI Agent
# Stock Market AI Agent

This project is a Django REST API that:
- Fetches the latest stock prices using DuckDuckGo search.
- Uses LangChain and OpenAI API to provide stock recommendations (Buy/Sell/Hold).
- Provides REST API endpoints to fetch stock data and recommendations.

---


---

## Prerequisites
- Python 3.8+
- Django & Django REST Framework
- OpenAI API Key (for stock recommendations)

---

## Setup & Installation
### Clone the Repository
```sh
git clone https://github.com/harsh9690/Stock_Market.git
cd stock_agent
```

### Create & Activate Virtual Environment
#### Windows (CMD)
```sh
python -m venv venv
venv\Scripts\activate
```
#### Windows (PowerShell)
```sh
python -m venv venv
venv\Scripts\Activate.ps1
```


### Apply Database Migrations
```sh
python manage.py migrate
```

### Set Up OpenAI API Key
1. Create a `.env` file in the project root:
   ```sh
   touch .env
   ```
2. Add your OpenAI API key in `.env`:
   ```ini
   OPENAI_API_KEY=your_openai_api_key_here
   ```


---

## API Endpoints


| GET | `/api/stock/{ticker}/` | Fetch stock price 
| GET | `/api/recommend/{ticker}/` | Fetch stock price & AI-based recommendation |

---

## Testing the APIs
You can test using Postman, cURL, or a web browser.

### Fetch Stock Price
#### cURL Command:
```sh
curl http://127.0.0.1:8000/api/stock/AAPL/
```
#### Expected Response:
```json
{
  "ticker": "AAPL",
  "price": "Fetching logic to be implemented"
}
```

---

### Get AI Recommendation
#### cURL Command:
```sh
curl http://127.0.0.1:8000/api/recommend/AAPL/
```
#### Expected Response:
```json
{
  "ticker": "AAPL",
  "price": "Fetching logic to be implemented",
  "recommendation": "You should buy this stock based on the current trend."
}
```

---

## Environment Variables
Set your OpenAI API Key in `.env` as follows:
```ini
OPENAI_API_KEY=your_openai_api_key_here
```

---


---


## Troubleshooting
1. If `requests` is not found:
   ```sh
   pip install requests
   ```
2. If `ModuleNotFoundError: No module named 'rest_framework'`:
   ```sh
   pip install djangorestframework
   ```
3. If Django is not installed:
   ```sh
   pip install django
   ```

---



---


