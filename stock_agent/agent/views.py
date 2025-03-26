from rest_framework.decorators import api_view
from rest_framework.response import Response
from .stock_fetcher import get_stock_price
from .recommendation import get_recommendation

@api_view(['GET'])
def fetch_stock(request, ticker):
    stock_data = get_stock_price(ticker)
    return Response(stock_data)

@api_view(['GET'])
def stock_recommendation(request, ticker):
    stock_data = get_stock_price(ticker)
    if "error" in stock_data:
        return Response(stock_data)
    recommendation = get_recommendation(ticker, stock_data["price"])
    stock_data["recommendation"] = recommendation
    return Response(stock_data)
