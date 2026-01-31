# Project 2: Social Media AI Agent with Approval

## What is This?
An AI assistant that helps you create social media posts, but requires your approval before posting anything. This teaches you about AI-human collaboration and safety controls.

## What You'll Learn
- Using AI to generate creative content
- Implementing approval workflows
- AI content moderation
- Ethical AI usage

## Prerequisites
- Python 3.8 or higher
- Basic Python knowledge
- OpenAI API key (get one at https://platform.openai.com)
- Optional: Twitter/X API credentials (for actual posting)

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

### Step 3: Run the Agent
```bash
python social_agent.py
```

### Step 4: Generate Posts
- Enter a topic or idea
- AI will generate a post
- Review and approve/reject
- Optionally save to file

## How It Works
1. **User Input**: You provide a topic or idea
2. **AI Generation**: Creates a social media post
3. **Preview**: Shows you the generated content
4. **Approval**: You decide to approve or reject
5. **Action**: Saves approved posts or discards rejected ones

## Files
- `social_agent.py`: Main application code
- `requirements.txt`: Python dependencies
- `approved_posts.txt`: Saved approved posts
- `.env`: Your API key (create this yourself)

## Features
- Multiple post styles (casual, professional, funny, informative)
- Character count limits
- Hashtag suggestions
- Emoji support
- Approval workflow

## Safety Features
- **Human-in-the-loop**: Nothing posts without approval
- **Content review**: You see everything before it's saved
- **Edit capability**: Modify AI suggestions
- **Audit trail**: All approved posts are logged

## Tips for Beginners
- Start with simple topics
- Try different post styles
- Review all AI-generated content carefully
- Use this to learn what makes good content
- Never bypass the approval step

## Ethical Considerations
- Always review AI-generated content
- Don't use AI to spread misinformation
- Be transparent that content is AI-assisted
- Take responsibility for what you post
- Respect platform guidelines

## Next Steps
- Integrate with actual social media APIs
- Add scheduling features
- Create A/B testing capabilities
- Implement analytics
