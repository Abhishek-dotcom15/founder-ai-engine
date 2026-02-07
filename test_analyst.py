from rss_fetcher import get_news
from analyst import pick_best_article

articles = get_news()

best = pick_best_article(articles)

print("\n✅ SELECTED MARKET SHIFT:\n")
print(best)
