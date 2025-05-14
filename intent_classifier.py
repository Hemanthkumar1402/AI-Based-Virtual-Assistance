import re


def get_intent(user_input):
    user_input = user_input.lower()

    if "time" in user_input:
        return "time"
    elif "remind" in user_input or "reminder" in user_input:
        return "set_reminder"
    elif re.search(r"\b(who|what|when|where|why|how)\b", user_input):
        return "general_qa"
    elif re.search(r"[\d\+\-\*/\(\)]", user_input):
        return "calculator"
    elif "search" in user_input or "google" in user_input:
        return "search"
    elif "open" in user_input and any(app in user_input for app in ["whatsapp", "facebook", "instagram", "youtube", "linkedin", "twitter"]):
        return "open_app"
    elif "exit" in user_input or "quit" in user_input:
        return "exit"
    else:
        return "unknown"
