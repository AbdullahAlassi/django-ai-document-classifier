def classify_text(text):
    categories = {
        "Technology": ["software", "hardware", "AI", "machine learning", "deep learning", "data science", "cybersecurity", "IoT", "Blockchain", "quantum computing"],
        "Business": ["finance", "marketing", "management", "leadership", "entrepreneurship", "innovation", "strategy", "competition", "economy", "entrepreneurship"],
        "Health": ["medicine", "pharmacy", "dentistry", "nursing", "healthcare", "medicine", "pharmacy", "dentistry", "nursing", "healthcare"],
    }

    for category, keywords in categories.items():
        for word in keywords: 
            if word.lower() in text.lower():
                return category

    return "General"
    