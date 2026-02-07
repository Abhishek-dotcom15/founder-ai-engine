from rss_fetcher import get_news
from analyst import pick_best_article
from strategist import deep_analysis


articles = get_news()
best = pick_best_article(articles)

analysis = deep_analysis(best)

print("\n🔥 STRATEGIC ANALYSIS:\n")
print(analysis)
