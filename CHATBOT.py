print("Welcome to AI Chat Bot")
print("Type bye to exit")

while True:

    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi!")

    elif user == "hi":
        print("Bot: Hello!")

    elif user == "how are you":
        print("Bot: I am fine.")

    elif user == "what is your name":
        print("Bot: My name is AI Chat Bot")

    elif user == "who created you":
        print("Bot: I am created using Python")

    elif user == "bye":
        print("Bot: Goodbye")
        break

    else:
        print("Bot: Sorry, I can't understand")