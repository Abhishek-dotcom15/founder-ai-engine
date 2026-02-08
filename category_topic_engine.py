import random
from datetime import datetime

# Founder-grade category structure
CATEGORY_BANK = {

    "MARKET_INSIGHT": [
        "A major shift happening in AI that most businesses are underestimating",
        "Where AI will reshape industries faster than leaders expect",
        "The next competitive advantage AI is quietly creating"
    ],

    "CONTRARIAN": [
        "Why most companies are approaching AI completely wrong",
        "A dangerous belief executives still hold about automation",
        "Something the AI industry gets wrong"
    ],

    "FOUNDER_LESSON": [
        "A hard lesson learned while building AI systems",
        "Something operating in AI taught me that surprised even us",
        "A mistake that changed how we build automation"
    ],

    "PROOF": [
        "What actually changes inside a company after AI adoption",
        "An operational breakthrough we are seeing with automation",
        "What leaders notice immediately after implementing AI"
    ],

    "SYSTEMS": [
        "The internal AI structure modern companies will adopt",
        "Why automation must sit inside decision layers",
        "How AI is becoming operational infrastructure"
    ],

    "MYTH": [
        "A myth about AI costing companies time and money",
        "Why AI is not replacing jobs the way people think",
        "The biggest misunderstanding about automation"
    ],

    "FUTURE": [
        "What AI-native companies will look like in 3 years",
        "The future operating model of AI-driven businesses",
        "Where intelligent automation is heading next"
    ]
}


def get_today_topic():
    """
    Rotates categories automatically based on day-of-year.
    Prevents repetition.
    Makes your content feel strategically planned.
    """

    categories = list(CATEGORY_BANK.keys())

    day_number = datetime.utcnow().timetuple().tm_yday

    selected_category = categories[day_number % len(categories)]

    topic = random.choice(CATEGORY_BANK[selected_category])

    return topic, selected_category
