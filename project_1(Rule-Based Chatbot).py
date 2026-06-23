def chatbot():
    print("Chatbot started. Type 'exit' to quit.")
    
    # store predefined responses
    responses = {
        'hello': 'Hi there!',
        'hi': 'Hey! What can I help you with?',
        'who are you': 'I am a simple rule-based AI.',
        'how are you': 'Doing good!',
        'tell me a joke': 'Why do programmers prefer dark mode? Because light attracts bugs.',
        'bye': 'Catch you later!'
    }

    while True:
        user_input = input('You: ')
        
        # clean up the input
        clean_input = user_input.lower().strip()
        
        if clean_input == 'exit':
            print("Bot: Bye!")
            break
            
        # check dictionary for match, else use fallback
        reply = responses.get(clean_input, "I do not understand.")
        print(f"Bot: {reply}")

if __name__ == "__main__":
    chatbot()
