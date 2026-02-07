import feedparser


def get_news():

    feeds = [
        "https://news.google.com/rss/search?q=enterprise+AI",
        "https://news.google.com/rss/search?q=AI+automation+business",
        "https://news.google.com/rss/search?q=AI+startups+funding",
        "https://news.google.com/rss/search?q=generative+AI+companies"
    ]

    articles = []

    for url in feeds:

        feed = feedparser.parse(url)

        for entry in feed.entries[:5]:

            article = f"""
Title: {entry.title}
Summary: {entry.summary}
"""

            articles.append(article)

    return articles
