# Reddit Persona Extractor 🧠

This project extracts a detailed user persona from any public Reddit profile by analyzing their posts and comments using a Large Language Model (LLM).

---

## 🔧 Features

- ✅ Scrapes posts & comments from any public Reddit user
- ✅ Builds a psychological + behavioral persona
- ✅ Includes LLM-backed citations for every insight
- ✅ Fully automated, clean output saved to `.txt` files

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/Reddit_Persona_Extractor.git
cd Reddit_Persona_Extractor

---

Install requirements :-

pip install -r requirements.txt

---

Create a .env file with your Reddit API credentials:

REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=PersonaExtractor by u/your_username

OPENROUTER_API_KEY=your_openrouter_api_key
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1/chat/completions
OPENROUTER_MODEL=meta-llama/llama-3-70b-instruct

---

How to run 

python main.py

--- 

Sample for u/DeepakBonagiri

Based on the provided Reddit posts and comments, I've generated a detailed persona:

**Age Range:** 18-25 years old

**Gender:** Male (Comment 23: "Will link save me? I am a guy")

**Hobbies & Interests:**

1. Gaming (Genshin Impact, Pokémon Unite, and other games)
2. Anime and manga (Tokidoki Bosotto Roshia, OshiNoKo, Fairy Tail)
3. Cricket (IPL teams: Sunrisers Hyderabad, Punjab Kings)
4. Memes and humor (participates in meme subreddits and creates own memes)
