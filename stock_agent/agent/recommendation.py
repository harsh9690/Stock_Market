import openai

def get_recommendation(ticker, price):
    """Use OpenAI API to generate a buy/sell/hold recommendation."""
    openai.api_key = "YOUR_OPENAI_API_KEY"  
    prompt = f"The current price of {ticker} is {price}. Should I buy, sell, or hold?"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]
