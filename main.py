from email_sender import send_email

from rss_fetcher import get_news
from analyst import pick_best_article
from strategist import deep_analysis
from pov_generator import generate_pov
from founder_writer import write_founder_post


def run_founder_engine():

    print("Scanning the market...")
    news = get_news()

    print("Identifying the real shift...")
    best_article = pick_best_article(news)

    print("Thinking strategically...")
    analysis = deep_analysis(best_article)

    print("Forming executive belief...")
    pov = generate_pov(analysis)

    print("Writing founder post...")
    post = write_founder_post(analysis, pov)

    print("\n\n========= FOUNDER POST =========\n")
    print(post)
    send_email(post)

    print("\n================================\n")


if __name__ == "__main__":
    run_founder_engine()
