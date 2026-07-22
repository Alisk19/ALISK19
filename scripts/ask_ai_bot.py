import os
import random
from github import Github

def generate_response(title, body):
    # Simulated AI logic (Rule-based)
    text = (title + " " + body).lower()
    
    responses = [
        "That's an excellent question! While my creator (Muhammed) is away building scalable data pipelines, I can tell you that exploring advanced AI architectures is always on our roadmap.",
        "Hello! I am Muhammed's automated Data Science Bot. He's currently training a deep learning model, but I'll make sure he sees this issue soon!",
        "Fascinating! The intersection of Data Engineering and AI is exactly what we specialize in here. Thanks for reaching out!",
        "Beep Boop. I've analyzed your request using my rule-based simulated neural network. Conclusion: Muhammed will definitely want to chat with you about this.",
        "Thanks for the ping! If this is regarding a Data Science or MLOps role, you're in the right place."
    ]
    
    if "hire" in text or "job" in text or "opportunity" in text:
        return "It sounds like you're reaching out about an opportunity! Muhammed is always open to discussing Data Science and AI Engineering roles. He'll get back to you shortly."
    if "model" in text or "machine learning" in text:
        return "Ah, Machine Learning! That's our favorite topic. We love building predictive models and optimizing architectures."
        
    return random.choice(responses)

def main():
    token = os.getenv('GITHUB_TOKEN')
    issue_number = os.getenv('ISSUE_NUMBER')
    title = os.getenv('ISSUE_TITLE', '')
    body = os.getenv('ISSUE_BODY', '')
    
    repo_name = os.getenv('GITHUB_REPOSITORY')
    
    if not token or not repo_name or not issue_number:
        print("Missing required environment variables (GITHUB_TOKEN, GITHUB_REPOSITORY, ISSUE_NUMBER)")
        return
        
    issue_number = int(issue_number)
    
    g = Github(token)
    repo = g.get_repo(repo_name)
    issue = repo.get_issue(number=issue_number)
    
    reply = generate_response(title, body)
    formatted_reply = f"🤖 **Ask-My-AI Automated Response:**\n\n> {reply}\n\n*(Note: This is a simulated AI running via GitHub Actions!)*"
    
    issue.create_comment(formatted_reply)
    print(f"Commented on issue #{issue_number}")

if __name__ == "__main__":
    main()
