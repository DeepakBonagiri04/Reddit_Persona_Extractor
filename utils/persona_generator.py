import os
import httpx
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL")

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "HTTP-Referer": "https://github.com/your-username/Reddit_Persona_Extractor",  # Update if needed
    "Content-Type": "application/json"
}

def format_prompt(posts, comments):
    text = "You are an expert in building psychological user personas. Below are Reddit posts and comments from a user. Based on these, generate a detailed persona including:\n\n"
    text += "- Age Range\n- Gender (if guessable)\n- Political Views\n- Hobbies & Interests\n- Personality Traits\n- Writing Style\n- Common Topics\n- Profession (if guessable)\n- Mental State (if inferable)\n\n"
    text += "Cite which post or comment supports each insight using numbered bullets.\n\n"

    text += "### Posts:\n"
    for i, post in enumerate(posts, 1):
        combined = f"Title: {post['title']}\nContent: {post['selftext']}\nURL: {post['url']}\nScore: {post['score']}\n\n"
        text += f"[Post {i}]\n{combined}"

    text += "\n### Comments:\n"
    for i, comment in enumerate(comments, 1):
        text += f"[Comment {i}] {comment['body']} (Score: {comment['score']})\nLink: {comment['link']}\n\n"

    return text

async def query_openrouter(prompt):
    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                OPENROUTER_BASE_URL,
                headers=HEADERS,
                json={
                    "model": OPENROUTER_MODEL,
                    "messages": [
                        {"role": "system", "content": "You are a helpful AI assistant."},
                        {"role": "user", "content": prompt}
                    ]
                }
            )
            print("Status code:", response.status_code)
            print("Raw response text:", response.text[:500])  # Show preview

            response.raise_for_status()
            result = response.json()
            return result["choices"][0]["message"]["content"]

    except httpx.HTTPStatusError as e:
        print("❌ HTTP error:", e)
    except Exception as e:
        print("❌ General error:", e)

    return "[Error] Could not generate persona due to LLM failure."

def save_persona_to_file(username, persona_text):
    os.makedirs("outputs", exist_ok=True)
    filename = f"outputs/{username}_persona.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(persona_text)
    print(f"[✓] Persona saved to {filename}")