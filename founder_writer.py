from gemini_client import client
import os
from dotenv import load_dotenv

load_dotenv()

COMPANY = os.getenv("COMPANY_NAME")

with open("founder_style.txt", "r", encoding="utf-8") as file:
    FOUNDER_STYLE = file.read()


def write_founder_post(analysis, pov):

    prompt = f"""
You are the founder of {COMPANY}.

Your role is NOT to market.
Your role is to demonstrate deep market understanding.

Below is your writing identity:

{FOUNDER_STYLE}

-----------------------------------

Strategic context:

{analysis}

Founder belief:

{pov}

-----------------------------------

Write a HIGH-AUTHORITY LinkedIn post.

This should feel like it came from a founder operating at the front edge of AI transformation.

NOT a content creator.
NOT a consultant.
NOT a marketer.

A builder.

-----------------------------------

STRUCTURE:

• Start with a powerful one-line hook.
• Leave a blank line.
• Use very short paragraphs (1–2 lines).
• Optimize for mobile reading.
• Deliver insight → business implication → future signal.

-----------------------------------

🔥 SOFT PROMOTION RULE (CRITICAL):

You MUST subtly position {COMPANY} as a company already working on these problems.

DO NOT advertise.

DO NOT pitch.

DO NOT use corporate phrases.

Instead, reference real-world observations like:

- “We’re seeing…”
- “In the systems we design…”
- “Companies working with us often discover…”
- “Inside high-performing teams…”
- “When automation is implemented correctly…”

The reader should naturally conclude that {COMPANY} understands the future and builds toward it.

Promotion must feel invisible.

-----------------------------------

STYLE RULES:

- 180–220 words MAX
- Extremely sharp
- No fluff
- No emojis
- No hashtags
- No markdown
- No motivational tone
- No buzzwords
- No theatrical language

Sound calm.
Sound intelligent.
Sound certain.

Write like a founder people trust when the market shifts.

End with a thoughtful question leaders would genuinely reflect on.
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    post = response.text

    # Safety cleanup
    post = post.replace("*", "")
    post = post.replace("#", "")
    post = post.replace("```", "")
    post = post.strip()

    return post
