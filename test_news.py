from rss_fetcher import get_news

articles = get_news()

for i, article in enumerate(articles[:3], 1):
    print(f"\n--- Article {i} ---")
    print(article)

