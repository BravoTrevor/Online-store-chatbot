import random
from fuzzywuzzy import process

# Welcome message
print("Welcome to your chatbot! Type 'exit' to end the chat.\n")

# FAQ responses
faq_responses = {
    "return policy": "Our return policy allows you to return products within 30 days of purchase.",
    "shipping time": "Shipping typically takes 3-5 business days for local orders.",
    "payment methods": "We accept credit cards, mobile payments, and cash on delivery.",
    "contact support": "You can contact our support team at support@example.com or call 123-456-7890."
}

# Greeting responses
greetings = ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]
greeting_responses = ["Hello! How can I assist you today?", "Hi there! Need help with something?", "Hey! What can I do for you?"]

# Small talk responses
small_talk = {
    "how are you": "I'm just a program, but I'm here to help!",
    "what's your name": "I'm your friendly chatbot assistant!",
    "what can you do": "I can answer FAQs, help with shopping, and more!"
}

# Product catalog (mock example for recommendations)
product_catalog = {
    "laptop": ["High-Performance Laptop", "Budget-Friendly Laptop", "Gaming Laptop"],
    "phone": ["Smartphone with Great Camera", "Budget Smartphone", "Gaming Smartphone"],
    "headphones": ["Noise-Cancelling Headphones", "Wireless Earbuds", "Budget Headphones"]
}

def recommend_products(category):
    """Recommend products based on category."""
    return product_catalog.get(category.lower(), [])

# Chat loop
while True:
    user_input = input("You: ").lower()
    if user_input == "exit":
        print("Chatbot: Goodbye! Have a great day!")
        break

    # Check for greetings
    if any(greet in user_input for greet in greetings):
        print(f"Chatbot: {random.choice(greeting_responses)}")
        continue

    # Check for small talk
    if user_input in small_talk:
        print(f"Chatbot: {small_talk[user_input]}")
        continue

    # Check for product recommendations
    if "recommend" in user_input:
        words = user_input.split()
        for word in words:
            if word in product_catalog:
                recommendations = recommend_products(word)
                if recommendations:
                    print(f"Chatbot: Here are some {word} recommendations: {', '.join(recommendations)}")
                else:
                    print(f"Chatbot: Sorry, I don't have recommendations for {word}.")
                break
        else:
            print("Chatbot: Could you specify what type of product you'd like recommendations for?")
        continue

    # Use fuzzy matching for FAQs
    best_match, score = process.extractOne(user_input, faq_responses.keys())
    if score > 70:  # Match threshold
        print(f"Chatbot: {faq_responses[best_match]}")
    else:
        # Fallback for unrecognized input
        random_responses = [
            "Hmm, I don't have an answer for that yet. Can you ask something else?",
            "I'm not sure about that. Maybe check our website for more details!",
            "Sorry, I don't understand. Can you try rephrasing your question?"
        ]
        print(f"Chatbot: {random.choice(random_responses)}")
