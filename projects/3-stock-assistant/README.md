# Project 3: Stock Data AI Assistant

## What is This?
An AI assistant that helps you understand stock market data. It fetches real stock information and explains it in simple terms. Perfect for learning about finance and AI together.

## What You'll Learn
- Working with financial APIs
- Processing real-time data with AI
- Creating conversational AI assistants
- Combining multiple data sources

## Prerequisites
- Python 3.8 or higher
- Basic Python knowledge
- OpenAI API key (get one at https://platform.openai.com)
- No stock API key needed (uses free Yahoo Finance data)

## Step-by-Step Guide

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Set Up Your API Key
Create a `.env` file in this directory:
```
OPENAI_API_KEY=your-api-key-here
```

### Step 3: Run the Assistant
```bash
python stock_assistant.py
```

### Step 4: Ask Questions
Ask questions about stocks like:
- "What's the current price of Apple stock?"
- "Show me Tesla's performance today"
- "Compare Microsoft and Google stocks"

## How It Works
1. **User Question**: You ask about a stock
2. **Fetch Data**: Gets current stock information
3. **AI Analysis**: AI analyzes and explains the data
4. **Simple Explanation**: Returns answer in easy-to-understand language

## Files
- `stock_assistant.py`: Main application code
- `requirements.txt`: Python dependencies
- `.env`: Your API key (create this yourself)

## Features
- Real-time stock prices
- Price change tracking
- Simple explanations
- Multiple stock comparisons
- Historical data (basic)

## Stock Symbols
Use standard stock ticker symbols:
- AAPL = Apple
- MSFT = Microsoft
- GOOGL = Google
- TSLA = Tesla
- AMZN = Amazon
- META = Meta (Facebook)

## Important Notes
⚠️ **This is for educational purposes only!**
- Not financial advice
- Data may have delays
- Always verify important information
- Consult professionals for investment decisions

## Tips for Beginners
- Start with well-known companies
- Ask simple questions first
- Learn ticker symbols gradually
- Compare different stocks
- Focus on understanding, not trading

## Example Questions
- "What is the current price of AAPL?"
- "How did TSLA perform today?"
- "Compare MSFT and GOOGL"
- "What's the market cap of AMZN?"
- "Explain the stock data for META"

## What You'll Understand
- Stock prices and changes
- Market capitalization
- Trading volume
- 52-week highs and lows
- Basic financial metrics

## Safety Features
- Clear disclaimer on startup
- Educational focus
- No trading functionality
- Read-only data access

## Next Steps
- Add charting capabilities
- Include news sentiment
- Track portfolio (paper trading)
- Add technical indicators
- Create alerts
