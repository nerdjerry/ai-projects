"""
Social Media AI Agent with Approval
====================================
An AI assistant that generates social media posts but requires your approval.
This demonstrates AI-human collaboration with safety controls.

Key Features:
- Generate posts on any topic
- Multiple writing styles
- Human approval required
- Safe and ethical AI use
"""

import os
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_social_post(topic, style="casual", max_length=280):
    """
    Generate a social media post using AI.
    
    Args:
        topic: The topic or idea for the post
        style: Writing style (casual, professional, funny, informative)
        max_length: Maximum character length (default 280 for Twitter/X)
    
    Returns:
        Generated post text
    """
    # Create style-specific instructions
    style_prompts = {
        "casual": "Write in a friendly, conversational tone",
        "professional": "Write in a professional, business tone",
        "funny": "Write in a humorous, entertaining tone",
        "informative": "Write in an educational, informative tone"
    }
    
    style_instruction = style_prompts.get(style, style_prompts["casual"])
    
    # Create the prompt
    prompt = f"""Create a social media post about: {topic}

Requirements:
- {style_instruction}
- Maximum {max_length} characters
- Engaging and attention-grabbing
- Include relevant hashtags (1-3)
- Can include emojis if appropriate

Generate only the post text, nothing else."""
    
    # Get AI response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a creative social media content creator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,  # Higher temperature for more creativity
        max_tokens=200
    )
    
    return response.choices[0].message.content.strip()


def review_post(post_text):
    """
    Check if a post is appropriate and safe.
    
    Args:
        post_text: The post to review
    
    Returns:
        tuple: (is_safe, issues) where is_safe is bool and issues is list of concerns
    """
    # Use AI to check for potential issues
    prompt = f"""Review this social media post for potential issues:

"{post_text}"

Check for:
- Offensive content
- Misinformation claims
- Promotional spam
- Privacy violations

If there are concerns, list them. If the post is fine, respond with "APPROVED".
Be strict but fair."""
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a content moderator focused on safety and ethics."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,  # Lower temperature for consistency
        max_tokens=150
    )
    
    result = response.choices[0].message.content.strip()
    
    if "APPROVED" in result.upper():
        return True, []
    else:
        return False, [result]


def save_approved_post(post_text, topic):
    """
    Save an approved post to a file.
    
    Args:
        post_text: The approved post
        topic: The topic it was about
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("approved_posts.txt", "a", encoding="utf-8") as f:
        f.write(f"\n{'='*60}\n")
        f.write(f"Timestamp: {timestamp}\n")
        f.write(f"Topic: {topic}\n")
        f.write(f"Post:\n{post_text}\n")


def get_style_choice():
    """
    Let user choose a writing style.
    
    Returns:
        Selected style
    """
    print("\nChoose a writing style:")
    print("1. Casual (friendly and conversational)")
    print("2. Professional (business-like)")
    print("3. Funny (humorous and entertaining)")
    print("4. Informative (educational)")
    
    while True:
        choice = input("\nEnter 1-4: ").strip()
        styles = {"1": "casual", "2": "professional", "3": "funny", "4": "informative"}
        
        if choice in styles:
            return styles[choice]
        print("Invalid choice. Please enter 1-4.")


def main():
    """
    Main function to run the social media agent.
    """
    print("=" * 60)
    print("Social Media AI Agent with Approval")
    print("=" * 60)
    print()
    print("This AI helps you create social media posts.")
    print("You'll review and approve each post before saving.")
    print()
    
    while True:
        print("-" * 60)
        
        # Get topic from user
        topic = input("\nEnter a topic for your post (or 'quit' to exit): ").strip()
        
        if topic.lower() in ['quit', 'exit', 'q']:
            print("\nGoodbye!")
            break
        
        if not topic:
            continue
        
        # Get style preference
        style = get_style_choice()
        
        print("\n🤖 Generating post...")
        
        # Generate the post
        try:
            post = generate_social_post(topic, style)
        except Exception as e:
        # Loop to allow regenerating new versions with same topic and style
        while True:
            print("\n🤖 Generating post...")
            
            # Generate the post
            try:
                post = generate_social_post(topic, style)
            except Exception as e:
                print(f"\n❌ Error generating post: {e}")
                break
            
            # Show the generated post
            print("\n" + "="*60)
            print("GENERATED POST:")
            print("="*60)
            print(post)
            print("="*60)
            print(f"\nCharacter count: {len(post)}")
            
            # AI content review
            print("\n🔍 Running safety check...")
            is_safe, issues = review_post(post)
            
            if not is_safe:
                print("\n⚠️  SAFETY CONCERNS DETECTED:")
                for issue in issues:
                    print(f"  - {issue}")
                print("\nThis post may need revision.")
            else:
                print("✅ Safety check passed")
            
            # Get user approval
            print("\n" + "-"*60)
            print("Do you approve this post?")
            print("1. Approve and save")
            print("2. Reject (discard)")
            print("3. Generate a new version")
            
            while True:
                decision = input("\nEnter 1-3: ").strip()
                
                if decision == "1":
                    # Approve and save
                    save_approved_post(post, topic)
                    print("\n✅ Post approved and saved to approved_posts.txt")
                    break
                elif decision == "2":
                    # Reject
                    print("\n🗑️  Post rejected and discarded")
                    break
                elif decision == "3":
                    # Generate new version
                    print("\n🤖 Generating new version...")
                    break
                else:
                    print("Invalid choice. Please enter 1-3.")
            
            # If user chose to generate a new version, repeat inner loop
            if decision == "3":
                continue
            
            # For approve or reject, go back to outer loop for a new topic
            break


if __name__ == "__main__":
    main()
