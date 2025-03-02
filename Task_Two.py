import re

def chatbot_response(user_input):
    responses = {
        "hi": "Hello! How can I help you today?",
        "how are you": "I'm just a chatbot, but I'm doing well!",
        "bye": "Goodbye! Have a great day!",
        "your name": "I'm a simple chatbot created in Python."
    }
    
    for pattern, response in responses.items():
        if re.search(pattern, user_input.lower()):
            return response
    
    return "I'm not sure how to respond to that."

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break
    print(f"Chatbot: {chatbot_response(user_input)}")
