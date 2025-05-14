def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    responses = {
        "hi": "Hello!",
        "hello": "Hi there!",
        "how are you": "I'm just a bot, but I'm doing great!",
        "what is your name": "I’m a mini Python chatbot 🤖.",
        "bye": "Goodbye! Have a nice day.",
        "thank you": "You're welcome!",
        "who created you": "I was created using Python by a human like you.",
        "help": "Try saying hi, how are you, or bye."
    }

    return responses.get(user_input, "🤖 Sorry, I don’t understand that.")

def main():
    print("💬 Mini Python Chatbot")
    print("Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower().strip() == "bye":
            print("Bot: Goodbye! 👋")
            break
        response = chatbot_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()