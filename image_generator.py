import urllib.parse


def generate_image_url(topic):
    """
    Generates a futuristic AI-style image based on the topic.
    Uses Pollinations (free, no API key).
    No storage required.
    """

    prompt = f"""
Futuristic, ultra-modern visualization representing:

{topic}

Style:
- cinematic lighting
- artificial intelligence theme
- highly detailed
- professional
- dark tech aesthetic
- no text
- no logos
- no watermark
"""

    encoded_prompt = urllib.parse.quote(prompt)

    image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"

    return image_url
