from rss_fetcher import get_news
from analyst import pick_best_article
from strategist import deep_analysis
from pov_generator import generate_pov
from founder_writer import write_founder_post


news = get_news()
best = pick_best_article(news)
analysis = deep_analysis(best)

pov = generate_pov(analysis)

post = write_founder_post(analysis, pov)

print("\n🔥 FOUNDER POST:\n")
print(post)
