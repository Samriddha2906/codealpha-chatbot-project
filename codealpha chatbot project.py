

def chatbot():
    print(" Chatbot: Hello! Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print(" Chatbot: Hi! How can I help you today?")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks for asking! ")
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a great day! ")
            break
        elif user_input == "your name":
            print(" Chatbot: I'm CodeAlpha Bot, your friendly assistant!")
        elif user_input == "":
            print(" Chatbot: Please type something...")
        else:
            print(" Chatbot: Sorry, I don't understand that.")
chatbot()
