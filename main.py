import os
from reddit_fetcher import get_user_data
from persona_generator import generate_persona

def process_user(url):
    username = url.strip("/").split("/")[-1]
    print(f"\n🔍 Processing user: {username}...")
    posts, comments = get_user_data(username)
    persona = generate_persona(username, posts, comments)

    output_dir = r"A:\intership\reddit-persona"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{username}.txt")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(persona)

    print(f"✅ Persona saved to:\n{output_path}")

if __name__ == "__main__":
    reddit_urls = [
        "https://www.reddit.com/user/kojied/",
        "https://www.reddit.com/user/Hungry-Move-6603/"
    ]

    for url in reddit_urls:
        process_user(url)
