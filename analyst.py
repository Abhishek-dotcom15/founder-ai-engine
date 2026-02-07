from gemini_client import client


def pick_best_article(articles):

    prompt = f"""
You are a senior technology analyst helping the founder of an AI & Automation company.

From the articles below, choose ONE that represents a REAL shift in how businesses operate.

Reject:
- Small product launches
- Incremental updates
- Marketing announcements
- Hype

ONLY choose news that signals:
- enterprise adoption
- workflow automation
- cost reduction via AI
- competitive advantage
- industry disruption

Articles:
{articles}

Return ONLY the selected article.

Then explain in 2 clear sentences WHY this matters for businesses.
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text
