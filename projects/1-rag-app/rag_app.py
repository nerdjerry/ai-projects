"""
Simple RAG (Retrieval Augmented Generation) App
================================================
This app lets you ask questions about your own documents using AI.

How it works:
1. Loads documents from the 'documents' folder
2. Splits them into smaller chunks
3. Creates embeddings (numerical representations)
4. Finds relevant chunks when you ask a question
5. Uses AI to generate an answer based on those chunks
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def load_documents(folder_path="documents"):
    """
    Load all text documents from the specified folder.
    
    Args:
        folder_path: Path to the folder containing .txt files
    
    Returns:
        List of tuples (filename, content)
    """
    documents = []
    doc_folder = Path(folder_path)
    
    # Create folder if it doesn't exist
    doc_folder.mkdir(exist_ok=True)
    
    # Read all .txt files
    for file_path in doc_folder.glob("*.txt"):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            documents.append((file_path.name, content))
    
    return documents


def split_into_chunks(text, chunk_size=500):
    """
    Split text into smaller chunks for better processing.
    
    Args:
        text: The text to split
        chunk_size: Approximate size of each chunk in characters
    
    Returns:
        List of text chunks
    """
    words = text.split()
    chunks = []
    current_chunk = []
    current_size = 0
    
    for word in words:
        current_chunk.append(word)
        current_size += len(word) + 1  # +1 for space
        
        if current_size >= chunk_size:
            chunks.append(' '.join(current_chunk))
            current_chunk = []
            current_size = 0
    
    # Add remaining words
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    
    return chunks


def create_embedding(text):
    """
    Create an embedding (numerical representation) of text.
    
    Args:
        text: Text to convert to embedding
    
    Returns:
        Embedding vector (list of numbers)
    """
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response.data[0].embedding


def cosine_similarity(vec1, vec2):
    """
    Calculate similarity between two vectors.
    
    Args:
        vec1, vec2: Embedding vectors to compare
    
    Returns:
        Similarity score (higher = more similar)
    """
    # Simple dot product (works well for normalized embeddings)
    return sum(a * b for a, b in zip(vec1, vec2))


def find_relevant_chunks(question, chunks_with_embeddings, top_k=3):
    """
    Find the most relevant chunks for a question.
    
    Args:
        question: The user's question
        chunks_with_embeddings: List of (chunk, embedding) tuples
        top_k: Number of relevant chunks to return
    
    Returns:
        List of most relevant chunks
    """
    # Get embedding for the question
    question_embedding = create_embedding(question)
    
    # Calculate similarity for each chunk
    similarities = []
    for chunk, chunk_embedding in chunks_with_embeddings:
        similarity = cosine_similarity(question_embedding, chunk_embedding)
        similarities.append((chunk, similarity))
    
    # Sort by similarity and get top results
    similarities.sort(key=lambda x: x[1], reverse=True)
    return [chunk for chunk, _ in similarities[:top_k]]


def generate_answer(question, context_chunks):
    """
    Generate an answer using AI based on relevant context.
    
    Args:
        question: The user's question
        context_chunks: Relevant text chunks to use as context
    
    Returns:
        AI-generated answer
    """
    # Combine chunks into context
    context = "\n\n".join(context_chunks)
    
    # Create prompt for the AI
    prompt = f"""Based on the following context, please answer the question.
If the answer is not in the context, say "I don't have enough information to answer that."

Context:
{context}

Question: {question}

Answer:"""
    
    # Get response from AI
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions based on the provided context."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )
    
    return response.choices[0].message.content


def main():
    """
    Main function to run the RAG app.
    """
    print("=" * 60)
    print("RAG App - Ask questions about your documents!")
    print("=" * 60)
    print()
    
    # Step 1: Load documents
    print("Loading documents...")
    documents = load_documents()
    
    if not documents:
        print("No documents found in the 'documents' folder.")
        print("Please add .txt files to the 'documents' folder and try again.")
        return
    
    print(f"Found {len(documents)} document(s):")
    for filename, _ in documents:
        print(f"  - {filename}")
    print()
    
    # Step 2: Split documents into chunks and create embeddings
    print("Processing documents and creating embeddings...")
    all_chunks_with_embeddings = []
    
    for filename, content in documents:
        chunks = split_into_chunks(content)
        for chunk in chunks:
            embedding = create_embedding(chunk)
            all_chunks_with_embeddings.append((chunk, embedding))
    
    print(f"Created {len(all_chunks_with_embeddings)} chunks")
    print()
    
    # Step 3: Interactive question-answering loop
    print("You can now ask questions! (Type 'quit' to exit)")
    print("-" * 60)
    print()
    
    while True:
        # Get user question
        question = input("Your question: ").strip()
        
        if question.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        if not question:
            continue
        
        print()
        print("Thinking...")
        
        # Find relevant chunks
        relevant_chunks = find_relevant_chunks(question, all_chunks_with_embeddings)
        
        # Generate answer
        answer = generate_answer(question, relevant_chunks)
        
        print()
        print("Answer:")
        print(answer)
        print()
        print("-" * 60)
        print()


if __name__ == "__main__":
    main()
