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

Now write a LinkedIn post expressing this belief naturally.

Do NOT perform.
Do NOT try to sound impressive.

Just communicate like a real founder would.

Follow natural structure:

• Future-focused hook  
• What happened  
• Business implications  
• What companies are missing  
• Soft authority mention of {COMPANY}  
• Thoughtful closing question  

-----------------------------------

HUMAN WRITING RULES:

- Sound written, not generated.
- Slight imperfection is GOOD.
- Avoid polished AI rhythm.
- Vary sentence flow.
- Use occasional sharp one-liners.
- No emojis.
- No hashtags.
- No motivational tone.
- No corporate fluff.

Protect the founder’s reputation for being right about the future.

Have conviction.

Max 220 words.
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    post = response.text

    # Remove markdown formatting
    post = post.replace("*", "")
    post = post.replace("#", "")
    post = post.replace("```", "")

    return post
