import datetime
import wikipedia
import re
import webbrowser
import os
from memory import save_reminder


def tell_time():
    now = datetime.datetime.now()
    return f"The current time is {now.strftime('%I:%M %p')}."


def set_reminder(text):
    save_reminder(text)
    return f"Reminder saved: {text}"


def fetch_wiki(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except:
        return "Sorry, I couldn't find that on Wikipedia."


def do_calculation(expression):
    try:
        if not re.match(r"^[\d\s\.\+\-\*/\(\)]+$", expression):
            return "Invalid characters in calculation."
        result = eval(expression)
        return f"The result is {result}"
    except:
        return "Sorry, I couldn't compute that."


def general_qa(query):
    return fetch_wiki(query)


def do_search(query):
    return f"Searching the web for: '{query}'...\nTry: https://www.google.com/search?q={query.replace(' ', '+')}"


def open_app(user_input):
    sites = {
        "whatsapp": "https://web.whatsapp.com",
        "facebook": "https://www.facebook.com",
        "instagram": "https://www.instagram.com",
        "youtube": "https://www.youtube.com",
        "linkedin": "https://www.linkedin.com",
        "twitter": "https://www.twitter.com",
        "maps": "https://www.google.com/maps"
    }

    apps = {
        "notepad": "notepad",
        "calculator": "calc",
        "paint": "mspaint",
        "cmd": "cmd",
        "email": "start outlook"  # or try "start mailto:" for default mail app
    }

    user_input = user_input.lower()

    for name, url in sites.items():
        if name in user_input:
            webbrowser.open(url)
            return f"Opening {name.capitalize()}..."

    for name, command in apps.items():
        if name in user_input:
            os.system(command)
            return f"Launching {name.capitalize()}..."

    return "Sorry, I don't recognize that app."


def fallback():
    return "I'm not sure how to help with that."
