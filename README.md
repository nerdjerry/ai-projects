# AI Projects - Beginner-Friendly Learning Repository

Welcome! This repository contains 5 beginner-friendly AI projects designed to help you learn and build AI applications. Each project includes simple Python templates, clear comments, detailed README files, step-by-step guides, and minimal dependencies.

## 🎯 Purpose

This repository prioritizes **clarity over complexity**. Each project is designed to:
- Be easy to understand for beginners
- Teach core AI concepts through hands-on practice
- Use minimal dependencies
- Include extensive comments and documentation
- Provide practical, real-world examples

## 📚 Projects

### 1. RAG App (Retrieval Augmented Generation)
**Location:** `projects/1-rag-app/`

Build an AI that answers questions using your own documents. Learn how to combine document retrieval with AI generation.

**What you'll learn:**
- Document processing and chunking
- Embeddings and vector search
- Retrieval Augmented Generation (RAG)
- Working with OpenAI API

### 2. Social Media AI Agent with Approval
**Location:** `projects/2-social-media-agent/`

Create an AI assistant that generates social media posts with human approval. Learn about AI-human collaboration and ethical AI use.

**What you'll learn:**
- AI content generation
- Approval workflows
- Content moderation
- Ethical AI principles

### 3. Stock Data AI Assistant
**Location:** `projects/3-stock-assistant/`

Build an AI that explains stock market data in simple terms. Combines real-time data with AI explanations.

**What you'll learn:**
- Working with financial APIs
- Real-time data processing
- AI-powered explanations
- Data interpretation

### 4. AI with Memory
**Location:** `projects/4-ai-memory/`

Create a conversational AI that remembers previous interactions across sessions. Learn how to build personalized AI experiences.

**What you'll learn:**
- Conversation memory management
- Context preservation
- Session persistence
- Personalized AI responses

### 5. Data Quality Copilot
**Location:** `projects/5-data-quality-copilot/`

Build an AI that analyzes CSV files and identifies data quality issues. Learn about data analysis and quality assessment.

**What you'll learn:**
- Data quality metrics
- CSV file processing
- AI-powered data analysis
- Automated reporting

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Basic Python knowledge
- OpenAI API key ([Get one here](https://platform.openai.com))

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/nerdjerry/ai-projects.git
   cd ai-projects
   ```

2. **Choose a project**
   ```bash
   cd projects/1-rag-app  # Or any other project
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key**
   Create a `.env` file:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

5. **Run the project**
   ```bash
   python rag_app.py  # Or the main file for your chosen project
   ```

## 📖 Learning Path

**Recommended order for beginners:**

1. **Start with Project 4 (AI with Memory)** - Simplest to understand conversational AI
2. **Then try Project 2 (Social Media Agent)** - Learn about content generation and approval
3. **Move to Project 1 (RAG App)** - Understand document-based AI
4. **Try Project 3 (Stock Assistant)** - Work with external data sources
5. **Finish with Project 5 (Data Quality Copilot)** - Apply AI to data analysis

## 💡 Tips for Success

- **Read the README first** - Each project has detailed documentation
- **Start small** - Run the examples before modifying code
- **Experiment** - Try different inputs and see what happens
- **Read the comments** - Code is heavily documented to help you learn
- **Ask questions** - Use the issues tab if you get stuck

## 🛠️ Common Setup

All projects use:
- **OpenAI API** for AI capabilities
- **python-dotenv** for environment variables
- **Minimal additional dependencies** - Each project lists its specific requirements

## 📝 Project Structure

Each project follows this structure:
```
project-name/
├── README.md           # Detailed project documentation
├── main_app.py         # Main application code (well-commented)
├── requirements.txt    # Python dependencies
├── .env.example        # Example environment variables
└── data/              # Sample data or documents (if applicable)
```

## 🤝 Contributing

Contributions are welcome! Please:
- Keep the beginner-friendly focus
- Maintain clear documentation
- Add comments to explain your code
- Test your changes

## 📄 License

This project is open source and available for educational purposes.

## ⚠️ Important Notes

- These projects are for **educational purposes**
- API calls to OpenAI will incur costs (typically minimal for learning)
- Always review AI-generated content
- Keep your API keys secure (never commit them to git)

## 🌟 Next Steps

After completing these projects, you can:
- Build your own AI applications
- Combine concepts from multiple projects
- Explore more advanced AI topics
- Share your creations with the community

---

**Happy Learning! 🎓**

If you find these projects helpful, please star ⭐ this repository!
