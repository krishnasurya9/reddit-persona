
# 🤖 Reddit-Based User Persona Generator

> This project generates structured user personas using Reddit data, powered by a local LLM (MythoMax-L2 13B) running through LM Studio.

---

## 📌 Project Overview

```yaml
Input:  Reddit user profile URL
Output: Persona text file with traits, goals, frustrations & citations
LLM:    MythoMax-L2-13B via LM Studio (offline, local)
````

---

## 📂 Your Folder Structure

```yaml
reddit-persona/
├── main.py             # Runs everything
├── persona_generator.py# Builds prompt & sends to local LLM
├── reddit_fetcher.py   # Scrapes Reddit posts & comments
├── prompts             # (Optional) May contain prompt templates
├── requirements        # List of dependencies
```

> 🔹 Note: Your `.txt` output files will be saved to `A:\intership\reddit-persona\` by default.

---

## ✅ Features

* Takes a Reddit profile URL (e.g., `https://www.reddit.com/user/kojied/`)
* Scrapes posts and comments using PRAW
* Generates structured persona using LangChain + local LLM
* Saves output to a `.txt` file
* Each trait/insight cites its original Reddit source

---

## 🔧 Setup Instructions

### 1. Create Virtual Environment (Optional)

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements
```

---

## 🧠 LM Studio Setup (MythoMax)

1. Download [LM Studio](https://lmstudio.ai/)
2. Open it and:

   * Go to **Models** → Download `MythoMax-L2-13B GGUF`
   * Use `Q4_K_M` or `Q6_K` quantization
3. Go to **"OpenAI API Server"** tab

   * Enable it at: `http://127.0.0.1:961`
4. Confirm that `/v1/completions` is working

Test with:

```python
import requests
print(requests.get("http://127.0.0.1:961/v1/models").json())
```

---

## 🚀 Running the Script

From your terminal:

```bash
python main.py
```

This will process:

```python
reddit_urls = [
    "https://www.reddit.com/user/kojied/",
    "https://www.reddit.com/user/Hungry-Move-6603/"
]
```

And output:

```
✅ Persona saved to:
A:\intership\reddit-persona\kojied.txt
```

---

## 📄 Output Example (kojied.txt)

```text
Name: kojied
Location: Likely India (mentions Noida, Delhi)
Traits:
- Observational
- Critical thinker

Frustrations:
• Urban chaos and development noise [Source: https://reddit.com/...]
• Concerns about quality of life in Delhi [Source: https://reddit.com/...]

Motivations:
• Wants calm living environment
• Cares about social issues

Goals:
• Highlight city planning issues
• Promote better urban awareness
```

---

## 🛠 Tech Stack

```yaml
Language: Python 3.10+
Libraries:
  - praw
  - langchain
  - requests
LLM:
  - LM Studio (offline)
  - MythoMax-L2-13B (GGUF)
```

---

## 👨‍💻 Author Info

```yaml
Name: p krishna surya

```

---

## 📌 Notes

* All data is publicly available via Reddit API
* LM Studio keeps everything offline and private
* No OpenAI API key required


