import requests
from langchain.llms.base import LLM
from langchain.prompts import PromptTemplate
from typing import Optional, List

class LMStudioLLM(LLM):
    endpoint: str = "http://127.0.0.1:961/v1/completions"
    model_name: str = "MythoMax-L2-13B"
    temperature: float = 0.7
    max_tokens: int = 1500

    @property
    def _llm_type(self) -> str:
        return "lmstudio"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        headers = {"Content-Type": "application/json"}
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "stop": stop
        }
        response = requests.post(self.endpoint, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()["choices"][0]["text"]

template = """
You are a personality analyst. Based on the Reddit content below, generate a user persona in this structured format:

---
Name: {username}
Age: [guess or unknown]
Occupation: [guess or unknown]
Status: [Single, Married, etc.]
Location: [guess or unknown]
Tier: [Activity level]
Archetype: [e.g., Creator, Explorer]

Traits:
- Personality Style (Introvert/Extrovert, etc.)
- Thinking Style
- Adaptability
- Behavior Type

Motivations:
- Convenience:
- Wellness:
- Speed:
- Preferences:
- Comfort:
- Dietary Needs:

Behavior & Habits:
• Trait or habit 1 [with source link]
• Trait or habit 2 [with source link]

Frustrations:
• Frustration 1 [with source link]
• Frustration 2 [with source link]

Goals & Needs:
• Goal 1
• Goal 2

Reddit Activity:
{user_data}
"""

prompt_template = PromptTemplate.from_template(template)
llm = LMStudioLLM()

def generate_persona(username, posts, comments):
    user_data = "\n".join(posts + comments)
    final_prompt = prompt_template.format(username=username, user_data=user_data)
    return llm._call(final_prompt)
