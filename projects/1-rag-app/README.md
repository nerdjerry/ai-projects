# Project 1: RAG App (Retrieval Augmented Generation)

## What is RAG?
RAG (Retrieval Augmented Generation) is a technique that allows AI to answer questions using your own documents. Instead of relying only on training data, the AI retrieves relevant information from your documents and uses it to generate accurate answers.

## What You'll Learn
- How to load and process text documents
- Creating embeddings (numerical representations of text)
- Searching for relevant information
- Combining retrieval with AI generation

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

### Step 3: Add Your Documents
Place text files in the `documents/` folder. The app will use these to answer questions.

### Step 4: Run the App
```bash
python rag_app.py
```

### Step 5: Ask Questions
The app will prompt you to ask questions about your documents.

## How It Works
1. **Load Documents**: Reads text files from the documents folder
2. **Split Text**: Breaks documents into smaller chunks
3. **Create Embeddings**: Converts text chunks to numerical vectors
4. **Store Vectors**: Saves embeddings for quick searching
5. **Query**: When you ask a question, finds relevant chunks
6. **Generate**: Uses AI to create an answer based on relevant chunks

## Files
- `rag_app.py`: Main application code
- `requirements.txt`: Python dependencies
- `documents/`: Place your text files here
- `.env`: Your API key (create this yourself)

## Tips for Beginners
- Start with small text files (1-2 pages)
- Ask specific questions about your documents
- The quality of answers depends on document quality
- Experiment with different types of documents

## Common Issues
- **No documents found**: Make sure you have .txt files in the documents/ folder
- **API key error**: Check your .env file has the correct key
- **Slow responses**: Large documents take longer to process
