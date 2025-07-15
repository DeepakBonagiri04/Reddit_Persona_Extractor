import praw
import os
from dotenv import load_dotenv
from pathlib import Path

# ✅ Force load .env manually
load_dotenv(dotenv_path=Path('.') / '.env')

def get_reddit_instance():
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )
    reddit.read_only = True  # ✅ Important for public data access
    return reddit

def scrape_user_data(username, limit=50):
    reddit = get_reddit_instance()
    redditor = reddit.redditor(username)

    posts = []
    comments = []

    for post in redditor.submissions.new(limit=limit):
        posts.append({
            "title": post.title,
            "selftext": post.selftext,
            "url": post.url,
            "score": post.score
        })

    for comment in redditor.comments.new(limit=limit):
        comments.append({
            "body": comment.body,
            "link": f"https://reddit.com{comment.permalink}",
            "score": comment.score
        })

    return posts, comments