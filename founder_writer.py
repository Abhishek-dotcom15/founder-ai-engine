from gemini_client import client
import os
from dotenv import load_dotenv

load_dotenv()

COMPANY = os.getenv("COMPANY_NAME")

# Load founder style memory
with open("founder_style.txt", "r", encoding="utf-8") as file:
    FOUNDER_STYLE = file.read()


def write_founder_post(analysis, pov):

    prompt = f"""
You are the founder of {COMPANY}.

Below is your writing style identity.

{FOUNDER_STYLE}

-----------------------------------

Your private executive belief:

{pov}

-----------------------------------

Strategic context:

{analysis}

-----------------------------------

Write a HIGH-IMPACT LinkedIn post expressing this belief.

STRICT RULES:

- Maximum 220 words
- Short paragraphs (1–2 lines)
- No markdown
- No asterisks
- No hashtags inside sentences
- No emojis
- Avoid corporate buzzwords
- Sound like a sharp, experienced founder
- Be opinionated but not dramatic
- Make it feel written, not generated
- End with a thoughtful question to drive engagement

Do NOT sound like AI.
Do NOT sound motivational.
Do NOT over-explain.

Protect the founder’s reputation for being right about the future.
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    post = response.text

    # Clean markdown formatting just in case the model ignores instructions
    post = post.replace("*", "")
    post = post.replace("#", "")
    post = post.replace("```", "")
    post = post.strip()

    return post
