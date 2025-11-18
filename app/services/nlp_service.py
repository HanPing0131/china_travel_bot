def answer_travel_question(question: str) -> str:
    """
    Very simple rule-based demo for General China Travel Q&A.
    Later you can replace this with a real LLM or API call.
    """
    q = question.lower()

    if "visa" in q:
        return (
            "Visa requirements for China depend on your nationality and travel purpose. "
            "Most tourists need to apply for a visa in advance at a Chinese embassy or consulate. "
            "Always check the latest official information before you travel."
        )
    if "best time" in q or "when to go" in q:
        return (
            "Generally, the best time to visit many parts of China is spring (April–May) and autumn (September–October). "
            "These seasons usually have more comfortable temperatures and less extreme weather."
        )
    if "train" in q or "high-speed" in q:
        return (
            "China has an extensive high-speed rail network. You can buy tickets online or at the station. "
            "It is recommended to book in advance during holidays and peak seasons."
        )
    if "payment" in q or "alipay" in q or "wechat pay" in q:
        return (
            "In China, mobile payment such as Alipay and WeChat Pay are very common. "
            "However, many places still accept cash and bank cards, especially in big cities and tourist areas."
        )
    if "safety" in q:
        return (
            "Most major Chinese cities are relatively safe for tourists, especially in busy areas. "
            "Still, you should follow normal travel safety practices, such as keeping an eye on your belongings."
        )

    # Default generic answer
    return (
        "This is a simple demo answer. For your question about traveling in China, please consider:\n"
        "- City and region (north, south, coastal, inland)\n"
        "- Season and weather\n"
        "- Budget and travel style (city, nature, food, culture)\n"
        "You can ask more specific questions such as visa, transportation, safety, or best time to visit."
    )
