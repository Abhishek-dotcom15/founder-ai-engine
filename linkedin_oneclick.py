import urllib.parse

def create_linkedin_post_url(post_text):

    encoded_text = urllib.parse.quote(post_text)

    url = f"https://www.linkedin.com/feed/?shareActive=true&text={encoded_text}"

    return url
