from gemini_client import client


def generate_pov(analysis):

    prompt = f"""
You are the founder of a serious AI & Automation company.

Based on the strategic analysis below, form a STRONG executive opinion.

NOT a summary.
NOT neutral.

Take a stance.

Decide something like:

- What is inevitable?
- What is misunderstood?
- What are most companies getting wrong?
- What will separate winners from losers?

Write 5–7 sharp sentences.

Sound like a founder thinking privately.
Not performing.
Not teaching.

Avoid buzzwords.
Avoid fluff.

Strategic analysis:
{analysis}
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text
