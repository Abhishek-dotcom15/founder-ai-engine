from gemini_client import client

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain AI in one simple sentence."
)

print(response.text)
