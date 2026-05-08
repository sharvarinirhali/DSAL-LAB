# Elementary Customer Interaction Chatbot
# Works in terminal/console

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hello! Welcome to our service. How can I help you today?"
    elif "price" in user_input:
        return "Please tell me the product name, and I will provide the price."
    elif "book" in user_input:
        return "We have a wide range of books. Which one are you interested in?"
    elif "order" in user_input:
        return "Sure! Please provide the product name and quantity."
    elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
        return "Goodbye! Thank you for visiting. Have a great day!"
    else:
        return "Sorry, I didn't understand. Could you rephrase?"

def chat():
    print("🤖 Elementary Chatbot for Customer Interaction")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Bot:", chatbot_response(user_input))
            break
        response = chatbot_response(user_input)
        print("Bot:", response)

# Run the chatbot
chat()
