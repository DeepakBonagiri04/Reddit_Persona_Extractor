import asyncio
import os
from dotenv import load_dotenv
from pathlib import Path

from utils.reddit_scraper import scrape_user_data
from utils.persona_generator import format_prompt, query_openrouter, save_persona_to_file

# ✅ Force load .env manually
load_dotenv(dotenv_path=Path('.') / '.env')

def main():
    print("🔍 Reddit Persona Extractor")
    username = input("Enter Reddit username : ").strip()

    print(f"\n[1] Scraping Reddit user: {username}")
    posts, comments = scrape_user_data(username)

    if not posts and not comments:
        print("⚠️ No activity found for this user. Exiting.")
        return

    print(f"[✓] Fetched {len(posts)} posts and {len(comments)} comments.")

    print("\n[2] Building persona using LLM...")
    prompt = format_prompt(posts, comments)

    persona_text = asyncio.run(query_openrouter(prompt))

    print("[✓] Persona generated!")

    print("\n[3] Saving result to file...")
    save_persona_to_file(username, persona_text)

    print("\n🎉 Done! Check the `outputs` folder.\n")

if __name__ == "__main__":
    main()