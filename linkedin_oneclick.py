import urllib.parse


# Creates the ONE-CLICK post URL
def create_linkedin_post_url(post_text):

    encoded_post = urllib.parse.quote(post_text)

    url = f"https://www.linkedin.com/feed/?shareActive=true&text={encoded_post}"

    return url


# 🔥 NEW — Creates the EMAIL BUTTON
def create_linkedin_button(post_text):

    post_url = create_linkedin_post_url(post_text)

    button_html = f"""
        <div style="margin-top:35px; text-align:center;">
            <a href="{post_url}" target="_blank"
                style="
                    background-color:#0A66C2;
                    color:white;
                    padding:16px 28px;
                    font-size:18px;
                    border-radius:8px;
                    text-decoration:none;
                    font-weight:bold;
                    display:inline-block;
                ">
                👉 Post on LinkedIn
            </a>
        </div>
    """

    return button_html
