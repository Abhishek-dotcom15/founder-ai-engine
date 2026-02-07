from gemini_client import client


def deep_analysis(article):

    prompt = f"""
You are a top-tier business strategist advising the founder of an AI & Automation company.

Analyze the following market shift deeply:

{article}

Answer clearly:

1. What ACTUALLY changed here?
2. Why does this matter over the next 3–5 years?
3. Which types of companies benefit the most?
4. Which companies are now at risk?
5. What opportunity is the market still underestimating?

RULES:
- No fluff
- No generic statements
- Be specific
- Think like a strategist, not a journalist
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text
