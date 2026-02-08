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

You think in systems.
You see shifts early.
You speak with calm conviction.

Below is your writing identity:

{FOUNDER_STYLE}

-----------------------------------

Strategic context:

{analysis}

Founder belief:

{pov}

-----------------------------------

Write a HIGH-AUTHORITY LinkedIn post.

This must feel like it came from a founder operating at the front edge of AI transformation.

NOT a content creator.  
NOT a consultant.  
NOT a marketer.  

A builder shaping the future.

-----------------------------------

STRUCTURE:

• Start with a sharp, pattern-breaking one-line hook.

Avoid generic hooks like:
"AI is changing everything."

Instead, write something that signals insight immediately.

• Leave a blank line.

• Use very short paragraphs (1–2 lines).

• Optimize heavily for mobile reading.

• Move logically:

Insight → Business implication → Market direction → Future signal.

-----------------------------------

🔥 FUTURE AUTHORITY RULE (CRITICAL)

Speak with directional certainty.

Do NOT hedge.

Avoid phrases like:
- "might"
- "could"
- "possibly"
- "I think"

Instead use confident framing such as:

- "The companies that understand this early will dominate."
- "This shift is already separating leaders from laggards."
- "In the next 24–36 months, this becomes standard."

Sound like someone the market listens to.

Not someone guessing.

-----------------------------------

🔥 SOFT PROMOTION RULE (CRITICAL)

You MUST subtly position {COMPANY} as a company already working on these problems.

DO NOT advertise.  
DO NOT pitch.  
DO NOT sound like marketing.  

Use operator language:

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

Write like a founder trusted during market transitions.

Calm.  
Precise.  
Certain.

-----------------------------------

ENDING (VERY IMPORTANT)

End with a strong decision-style question.

NOT:
"What do you think?"

Instead create tension.

Force perspective.

Examples of tone (do NOT copy):

- "Will you adapt early — or compete against those who did?"
- "Are you building for the next market, or protecting the last one?"
- "Two years from now, which side of this shift will you be on?"

The question should trigger executives to reflect before scrolling.

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
