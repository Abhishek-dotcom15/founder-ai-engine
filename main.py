from email_sender import send_email

from rss_fetcher import get_news
from analyst import pick_best_article
from strategist import deep_analysis
from pov_generator import generate_pov
from founder_writer import write_founder_post
from linkedin_oneclick import create_linkedin_post_url
from category_topic_engine import get_today_topic


import random


def run_founder_engine():

    print("Starting Founder Engine...\n")

    # 🔥 Decide content mode (VERY SMART LAYER)
    # 60% News आधारित
    # 40% Founder-category based

    use_news = random.random() < 0.6

    if use_news:

        print("Scanning the market...")
        news = get_news()

        print("Identifying the real shift...")
        best_article = pick_best_article(news)

        print("Thinking strategically...")
        analysis = deep_analysis(best_article)

        print("Forming executive belief...")
        pov = generate_pov(analysis)

    else:

        print("Running Category Brain...")

        topic, category = get_today_topic()

        print(f"Selected Category: {category}")
        print(f"Topic: {topic}")

        analysis = topic
        pov = f"As the founder of { 'Brillinity' }, here is my operator perspective on: {topic}"

    print("Writing founder post...")
    post = write_founder_post(analysis, pov)

    linkedin_url = create_linkedin_post_url(post)

    print("\n✅ ONE-CLICK LINKEDIN POST:")
    print(linkedin_url)

    print("\n\n========= FOUNDER POST =========\n")
    print(post)

    # Keep email as safety fallback
    send_email(post)

    print("\n================================\n")


if __name__ == "__main__":
    run_founder_engine()
