"""
Stock Data AI Assistant
========================
An AI assistant that helps you understand stock market data.
Uses real stock information and explains it in simple terms.

Key Features:
- Real-time stock prices
- AI-powered explanations
- Multiple stock comparisons
- Beginner-friendly interface

DISCLAIMER: This is for educational purposes only. Not financial advice.
"""

import os
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI
import yfinance as yf

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_stock_data(symbol):
    """
    Fetch stock data for a given symbol.
    
    Args:
        symbol: Stock ticker symbol (e.g., 'AAPL', 'MSFT')
    
    Returns:
        Dictionary with stock information, or None if error
    """
    try:
        # Create ticker object
        ticker = yf.Ticker(symbol.upper())
        
        # Get current info
        info = ticker.info
        
        # Get today's data
        hist = ticker.history(period="1d")
        
        if hist.empty:
            return None
        
        current_price = hist['Close'].iloc[-1]
        
        # Prepare data dictionary
        data = {
            'symbol': symbol.upper(),
            'name': info.get('longName', symbol.upper()),
            'current_price': round(current_price, 2),
            'previous_close': info.get('previousClose', 0),
            'open': info.get('open', 0),
            'day_high': info.get('dayHigh', 0),
            'day_low': info.get('dayLow', 0),
            'volume': info.get('volume', 0),
            'market_cap': info.get('marketCap', 0),
            '52_week_high': info.get('fiftyTwoWeekHigh', 0),
            '52_week_low': info.get('fiftyTwoWeekLow', 0),
        }
        
        # Calculate change
        if data['previous_close'] > 0:
            change = current_price - data['previous_close']
            change_percent = (change / data['previous_close']) * 100
            data['change'] = round(change, 2)
            data['change_percent'] = round(change_percent, 2)
        else:
            data['change'] = 0
            data['change_percent'] = 0
        
        return data
        
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None


def format_large_number(num):
    """
    Format large numbers in a readable way.
    
    Args:
        num: Number to format
    
    Returns:
        Formatted string (e.g., "1.5M", "2.3B")
    """
    if num >= 1_000_000_000_000:
        return f"${num/1_000_000_000_000:.2f}T"
    elif num >= 1_000_000_000:
        return f"${num/1_000_000_000:.2f}B"
    elif num >= 1_000_000:
        return f"${num/1_000_000:.2f}M"
    else:
        return f"${num:,.0f}"


def create_stock_summary(data):
    """
    Create a text summary of stock data.
    
    Args:
        data: Stock data dictionary
    
    Returns:
        Formatted summary string
    """
    summary = f"""
Stock: {data['name']} ({data['symbol']})
Current Price: ${data['current_price']}
Change: ${data['change']} ({data['change_percent']:+.2f}%)
Previous Close: ${data['previous_close']}

Today's Trading:
- Open: ${data['open']}
- High: ${data['day_high']}
- Low: ${data['day_low']}
- Volume: {data['volume']:,}

52-Week Range:
- High: ${data['52_week_high']}
- Low: ${data['52_week_low']}

Market Cap: {format_large_number(data['market_cap'])}
"""
    return summary


def explain_with_ai(stock_data, user_question):
    """
    Use AI to explain stock data in simple terms.
    
    Args:
        stock_data: Stock information
        user_question: The user's original question
    
    Returns:
        AI-generated explanation
    """
    summary = create_stock_summary(stock_data)
    
    prompt = f"""The user asked: "{user_question}"

Here's the current stock data:
{summary}

Please provide a clear, beginner-friendly explanation that:
1. Directly answers their question
2. Explains what the numbers mean
3. Uses simple language
4. Avoids jargon or explains any necessary terms
5. Is encouraging and educational

Remember: This is for learning, not financial advice."""
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a friendly financial education assistant. Explain stock market concepts in simple terms. Always remind users this is educational, not financial advice."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=400
    )
    
    return response.choices[0].message.content


def extract_symbols(text):
    """
    Extract stock symbols from user input.
    
    Args:
        text: User's question
    
    Returns:
        List of potential stock symbols
    """
    # Simple extraction - look for uppercase words or known patterns
    words = text.upper().split()
    
    # Common stock symbols (you can expand this)
    known_symbols = [
        'AAPL', 'MSFT', 'GOOGL', 'GOOG', 'AMZN', 'TSLA', 'META', 
        'NVDA', 'AMD', 'INTC', 'NFLX', 'DIS', 'BA', 'GE', 'IBM'
    ]
    
    symbols = []
    for word in words:
        # Remove common punctuation
        clean_word = word.strip('.,!?;:')
        if clean_word in known_symbols or (len(clean_word) <= 5 and clean_word.isalpha()):
            symbols.append(clean_word)
    
    return symbols if symbols else []


def main():
    """
    Main function to run the stock assistant.
    """
    print("=" * 60)
    print("Stock Data AI Assistant")
    print("=" * 60)
    print()
    print("⚠️  EDUCATIONAL USE ONLY - NOT FINANCIAL ADVICE")
    print()
    print("Ask me about stocks! Examples:")
    print("  - 'What's the price of AAPL?'")
    print("  - 'How is TSLA doing today?'")
    print("  - 'Tell me about Microsoft stock (MSFT)'")
    print()
    
    while True:
        print("-" * 60)
        question = input("\nYour question (or 'quit' to exit): ").strip()
        
        if question.lower() in ['quit', 'exit', 'q']:
            print("\nGoodbye! Happy learning!")
            break
        
        if not question:
            continue
        
        # Extract stock symbols from question
        symbols = extract_symbols(question)
        
        if not symbols:
            print("\n❓ I couldn't find a stock symbol in your question.")
            print("Please include a ticker symbol (e.g., AAPL, TSLA, MSFT)")
            continue
        
        # For now, use the first symbol found
        symbol = symbols[0]
        
        print(f"\n🔍 Fetching data for {symbol}...")
        
        # Get stock data
        stock_data = get_stock_data(symbol)
        
        if not stock_data:
            print(f"\n❌ Couldn't find data for {symbol}")
            print("Make sure you're using a valid stock ticker symbol.")
            continue
        
        # Get AI explanation
        print("\n💭 Analyzing...")
        explanation = explain_with_ai(stock_data, question)
        
        # Display results
        print("\n" + "="*60)
        print("ANSWER:")
        print("="*60)
        print(explanation)
        print("\n" + "="*60)
        print(f"\nData as of: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("⚠️  For educational purposes only")


if __name__ == "__main__":
    main()
