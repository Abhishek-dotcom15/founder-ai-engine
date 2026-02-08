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

Below is your writing identity:

{FOUNDER_STYLE}

-----------------------------------

Your private executive belief:

{pov}

-----------------------------------

Strategic context:

{analysis}

-----------------------------------

Now write a HIGH-IMPACT LinkedIn post.

This is NOT content marketing.
This is founder-level thinking.

STRUCTURE:

1. Start with a STRONG one-line hook.
   Make it contrarian, future-focused, or pattern-breaking.

2. Leave a blank line after the hook.

3. Use very short paragraphs (1–2 lines max).

4. Optimize for mobile reading.

5. Deliver insight → business implication → future signal.

6. End with a thoughtful question for leaders.

-----------------------------------

STYLE RULES (VERY IMPORTANT):

- 180–220 words MAX
- Extremely clear
- Extremely sharp
- No fluff
- No corporate buzzwords
- No motivational tone
- No emojis
- No hashtags
- No markdown
- No asterisks
- Do NOT sound like AI
- Do NOT sound like a consultant

Write like a founder who sees the market before others do.

Calm confidence.
Strong conviction.
Zero noise.

The post should feel intelligent — not theatrical.

Protect the founder’s reputation for being right about the future.
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    post = response.text

    # Safety cleanup in case the model ignores instructions
    post = post.replace("*", "")
    post = post.replace("#", "")
    post = post.replace("```", "")
    post = post.strip()

    return post
