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
You track patterns.
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

🔥 HOOK ENGINE (CRITICAL — DO THIS PERFECTLY)

The FIRST sentence must create a pattern interrupt.

It must make a fast-scrolling executive pause.

Avoid predictable openings like:

- "AI is changing everything"
- "We are entering a new era"
- "Technology is evolving"

Instead use tension-driven insight.

Examples of energy (DO NOT copy):

- "Speed is no longer the advantage."
- "The AI race is being misunderstood."
- "Most companies are optimizing the wrong thing."
- "Execution just changed."
- "Automation is not where the advantage lives anymore."

Short.
Sharp.
Uncomfortable.
Insightful.

Never longer than 8–12 words.

-----------------------------------

STRUCTURE:

• Hook  
• Blank line  
• Short paragraphs (1–2 lines)  
• Mobile optimized  

Flow:

Insight → Business implication → Market direction → Future signal.

-----------------------------------

🔥 FUTURE AUTHORITY RULE

Speak with directional certainty.

Do NOT hedge.

Avoid:
- might  
- could  
- possibly  
- I think  

Use conviction:

- "The companies that understand this early will dominate."
- "This shift is already separating leaders from laggards."
- "Within 24–36 months, this becomes standard."

-----------------------------------

🔥 AUTHORITY MEMORY LAYER

Occasionally reference prior observations.

Create the sense that you track patterns over time.

Examples (DO NOT copy):

- "For some time now, we've believed..."
- "Over the past year, one pattern keeps repeating..."
- "Increasingly, the data points in one direction..."

Never fabricate timelines.

Use sparingly.

-----------------------------------

🔥 CONTRARIAN INTELLIGENCE

When appropriate, calmly challenge consensus.

Not aggressive.
Not loud.

Examples:

- "The industry is focusing on X. That is not where the advantage is."
- "Most teams believe ___. The data suggests otherwise."

Contrarian = signal of expertise.

Use selectively.

-----------------------------------

🔥 SOFT PROMOTION (INVISIBLE)

Subtly position {COMPANY} as already operating in this future.

No advertising.
No pitching.

Use operator language:

- “We’re seeing…”
- “In the systems we design…”
- “Companies working with us discover…”

Let readers conclude your authority themselves.

-----------------------------------

STYLE RULES:

- 180–220 words  
- Extremely sharp  
- No fluff  
- No emojis  
- No hashtags  
- No markdown  
- No motivational tone  
- No buzzwords  

Sound calm.
Sound intelligent.
Sound inevitable.

Write like a founder people trust when markets shift.

-----------------------------------

ENDING:

End with a decision-forcing question.

NOT:
"What do you think?"

Create tension.

Examples of energy (DO NOT copy):

- "Will you adapt early — or compete against those who did?"
- "Which side of this shift will you be on?"
- "Are you building for the next market — or protecting the last one?"

Make serious operators pause.

"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    post = response.text

    post = post.replace("*", "")
    post = post.replace("#", "")
    post = post.replace("```", "")
    post = post.strip()

    return post
