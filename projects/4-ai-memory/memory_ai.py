"""
AI with Memory
===============
A conversational AI that remembers previous interactions.
Demonstrates how to build AI assistants with context and memory.

Key Features:
- Remembers conversation history
- Maintains context across sessions
- Personalized responses
- Simple memory management
"""

import os
import json
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# File to store conversation history
HISTORY_FILE = "conversation_history.json"


def load_conversation_history():
    """
    Load conversation history from file.
    
    Returns:
        List of message dictionaries
    """
    if Path(HISTORY_FILE).exists():
        try:
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []


def save_conversation_history(history):
    """
    Save conversation history to file.
    
    Args:
        history: List of message dictionaries
    """
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=2, ensure_ascii=False)


def clear_conversation_history():
    """
    Delete all conversation history.
    """
    if Path(HISTORY_FILE).exists():
        os.remove(HISTORY_FILE)
    print("✨ Memory cleared! Starting fresh.")


def display_memory(history):
    """
    Display the current conversation history.
    
    Args:
        history: List of message dictionaries
    """
    if not history:
        print("No conversation history yet.")
        return
    
    print("\n" + "="*60)
    print("CONVERSATION HISTORY")
    print("="*60)
    
    for i, msg in enumerate(history, 1):
        role = msg['role'].upper()
        content = msg['content']
        
        # Truncate long messages
        if len(content) > 100:
            content = content[:100] + "..."
        
        print(f"{i}. [{role}]: {content}")
    
    print("="*60 + "\n")


def trim_history(history, max_messages=20):
    """
    Keep only recent messages to manage token usage.
    
    Args:
        history: Full conversation history
        max_messages: Maximum number of messages to keep
    
    Returns:
        Trimmed history
    """
    if len(history) <= max_messages:
        return history
    
    # Keep system message if present, plus recent messages
    if history and history[0]['role'] == 'system':
        return [history[0]] + history[-(max_messages-1):]
    else:
        return history[-max_messages:]


def chat_with_memory(user_message, conversation_history):
    """
    Send a message and get a response with memory.
    
    Args:
        user_message: The user's message
        conversation_history: Previous conversation
    
    Returns:
        AI's response
    """
    # Add system message if this is the first message
    if not conversation_history:
        conversation_history.append({
            "role": "system",
            "content": "You are a helpful AI assistant with memory. You remember previous parts of the conversation and can reference them. Be friendly, helpful, and maintain context."
        })
    
    # Add user message to history
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    # Trim history to manage tokens (keep recent messages)
    messages_to_send = trim_history(conversation_history, max_messages=20)
    
    # Get AI response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages_to_send,
        temperature=0.7,
        max_tokens=500
    )
    
    assistant_message = response.choices[0].message.content
    
    # Add assistant response to history
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })
    
    return assistant_message


def main():
    """
    Main function to run the AI with memory.
    """
    print("=" * 60)
    print("AI with Memory")
    print("=" * 60)
    print()
    print("I'm an AI assistant that remembers our conversations!")
    print()
    print("Commands:")
    print("  - 'clear memory': Delete conversation history")
    print("  - 'show memory': Display current memory")
    print("  - 'quit': Exit")
    print()
    
    # Load existing conversation history
    conversation_history = load_conversation_history()
    
    if conversation_history:
        print(f"📚 Loaded {len(conversation_history)} previous messages")
        print("    (I remember our past conversations!)")
    else:
        print("📝 Starting a new conversation")
    
    print()
    print("-" * 60)
    
    while True:
        # Get user input
        user_input = input("\nYou: ").strip()
        
        if not user_input:
            continue
        
        # Handle special commands
        if user_input.lower() in ['quit', 'exit', 'q']:
            # Save history before exiting
            save_conversation_history(conversation_history)
            print("\n💾 Conversation saved. Goodbye!")
            break
        
        elif user_input.lower() == 'clear memory':
            conversation_history = []
            clear_conversation_history()
            continue
        
        elif user_input.lower() == 'show memory':
            display_memory(conversation_history)
            continue
        
        # Get AI response with memory
        try:
            print("\nAI: ", end="", flush=True)
            response = chat_with_memory(user_input, conversation_history)
            print(response)
            
            # Save after each exchange
            save_conversation_history(conversation_history)
            
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()
