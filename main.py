from email_sender import send_email

from rss_fetcher import get_news
from analyst import pick_best_article
from strategist import deep_analysis
from pov_generator import generate_pov
from founder_writer import write_founder_post
from linkedin_oneclick import create_linkedin_post_url
from category_topic_engine import get_today_topic
from image_generator import generate_image_url

import random


def run_founder_engine():

    print("🚀 Starting Founder Engine...\n")

    use_news = random.random() < 0.6

    if use_news:

        print("🌍 Scanning the market...")
        news = get_news()

        print("🧠 Identifying the real shift...")
        best_article = pick_best_article(news)

        print("📊 Thinking strategically...")
        analysis = deep_analysis(best_article)

        print("🎯 Forming executive belief...")
        pov = generate_pov(analysis)

        # ✅ FIX — make system tolerant
        topic = str(best_article)

    else:

        print("🧭 Running Category Brain...")

        topic, category = get_today_topic()

        print(f"📌 Selected Category: {category}")
        print(f"🧠 Topic: {topic}")

        analysis = topic
        pov = f"As the founder of Brillinity, here is my operator perspective on: {topic}"

    print("✍️ Writing founder post...")
    post = write_founder_post(analysis, pov)

    print("🖼️ Generating contextual image...")
    image_url = generate_image_url(topic)

    post_with_image = f"{post}\n\n(Visual concept below)\n{image_url}"

    linkedin_url = create_linkedin_post_url(post_with_image)

    print("\n✅ ONE-CLICK LINKEDIN POST:")
    print(linkedin_url)

    print("\n\n========= FOUNDER POST =========\n")
    print(post_with_image)

    send_email(post_with_image)

    print("\n================================\n")


if __name__ == "__main__":
    run_founder_engine()
