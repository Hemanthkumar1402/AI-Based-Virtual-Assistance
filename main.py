from intent_classifier import get_intent
from actions import (
    tell_time,
    set_reminder,
    fetch_wiki,
    fallback,
    do_calculation,
    general_qa,
    do_search,
    open_app
)


def run_agent():
    print("Hi! I’m your AI Assistant. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        intent = get_intent(user_input)

        if intent == "time":
            print("AI:", tell_time())
        elif intent == "set_reminder":
            print("AI:", set_reminder(user_input))
        elif intent == "wiki":
            print("AI:", fetch_wiki(user_input))
        elif intent == "calculator":
            print("AI:", do_calculation(user_input))
        elif intent == "general_qa":
            print("AI:", general_qa(user_input))
        elif intent == "search":
            print("AI:", do_search(user_input))
        elif intent == "open_app":
            print("AI:", open_app(user_input))
        elif intent == "exit":
            print("AI: Goodbye!")
            break
        else:
            print("AI:", fallback())


if __name__ == "__main__":
    run_agent()
