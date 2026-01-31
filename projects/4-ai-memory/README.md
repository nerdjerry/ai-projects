# Project 4: AI with Memory

## What is This?
A conversational AI that remembers your previous interactions. Learn how to build AI assistants that maintain context and provide personalized experiences across sessions.

## What You'll Learn
- Implementing conversation memory
- Storing and retrieving context
- Building personalized AI experiences
- Managing conversation history

## Prerequisites
- Python 3.8 or higher
- Basic Python knowledge
- OpenAI API key (get one at https://platform.openai.com)

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
python memory_ai.py
```

### Step 4: Have a Conversation
- Talk to the AI naturally
- It remembers what you discussed
- Reference earlier topics
- Build on previous conversations

## How It Works
1. **User Message**: You send a message
2. **Load History**: Retrieves previous conversation
3. **AI Response**: Generates response with context
4. **Save History**: Stores the new exchange
5. **Persistence**: Memory saved across sessions

## Files
- `memory_ai.py`: Main application code
- `requirements.txt`: Python dependencies
- `conversation_history.json`: Stored conversations
- `.env`: Your API key (create this yourself)

## Features
- **Short-term Memory**: Remembers current conversation
- **Long-term Memory**: Saves across sessions
- **Context Awareness**: References previous topics
- **Personalization**: Learns about you over time
- **Clear Memory**: Option to start fresh

## Memory Types

### Short-term Memory
- Current conversation only
- Temporary context
- Cleared when you quit

### Long-term Memory
- Saved to file
- Persists across sessions
- Can be cleared manually

## Commands
- Regular messages: Just chat normally
- `clear memory`: Delete conversation history
- `show memory`: Display current history
- `quit`: Exit the program

## Tips for Beginners
- Try referencing earlier topics
- Test memory across different sessions
- Notice how context improves responses
- Experiment with clearing memory
- Ask follow-up questions

## Example Conversations
```
You: My name is Alex and I love Python
AI: Nice to meet you, Alex! Python is a great language...

[Later in conversation]
You: What's my favorite programming language?
AI: You mentioned you love Python!
```

## Privacy & Data
- Conversations stored locally only
- No data sent elsewhere (except OpenAI API)
- You control your data
- Can delete anytime

## How Memory Improves AI
- **Context**: AI understands what you're talking about
- **Personalization**: Tailored responses
- **Efficiency**: No need to repeat information
- **Natural Flow**: More human-like conversation

## Common Use Cases
- Personal assistant
- Learning companion
- Project discussion partner
- Brainstorming buddy

## Important Notes
- Memory uses local storage
- API calls cost money (minimal)
- Long conversations use more tokens
- Clear memory periodically for best results

## Next Steps
- Add user profiles
- Implement smart summarization
- Create topic-based memories
- Add memory search
- Build memory analytics
