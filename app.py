from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import random
import re
from rapidfuzz import process, fuzz

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

# Load simplified Amazon dataset
try:
    with open('amazon_products_simple.json', 'r', encoding='utf-8') as f:
        products = json.load(f)
except FileNotFoundError:
    print("Error: 'amazon_products_simple.json' not found. Please ensure the file exists.")
    products = []
except json.JSONDecodeError:
    print("Error: 'amazon_products_simple.json' is not a valid JSON file.")
    products = []

# Exit if no products are loaded
if not products:
    print("No products loaded. Exiting...")
    exit(1)

# Mock orders
orders = {
    "ORD123": {"status": "Delivered", "date": "2023-12-15"},
    "ORD456": {"status": "Shipped", "date": "2023-12-20"}
}

# Greetings and FAQs
GREETINGS = ["hello", "hi", "hey", "good morning", "good afternoon"]
GREETING_RESPONSES = ["Hello! How can I assist you today?", "Hi there! Need help?"]
FAQ_RESPONSES = {
    "return policy": "You can return items within 30 days of delivery.",
    "shipping time": "Standard shipping takes 3-5 business days.",
    "contact support": "Email us at support@example.com."
}

# Chatbot logic
def process_message(message):
    message = message.lower()
    
    # Handle greetings
    if any(greet in message for greet in GREETINGS):
        return random.choice(GREETING_RESPONSES)
    
    # Handle FAQs with fuzzy matching
    faq_match, score, _ = process.extractOne(message, FAQ_RESPONSES.keys())
    if score > 70:
        return FAQ_RESPONSES[faq_match]
    
    # Handle product search
    if "search" in message or "find" in message:
        query = re.sub(r"(search|find|\d+)", "", message).strip()
        num_results = int(re.search(r"\d+", message).group()) if re.search(r"\d+", message) else 3
        return search_products(query, num_results)
    
    # Handle order status
    order_id_match = re.search(r'\bORD\d{3}\b', message, re.IGNORECASE)
    if order_id_match:
        order_id = order_id_match.group().upper()
        return check_order_status(order_id)
    
    # Fallback for unrecognized input
    return "Sorry, I didn't understand! Try: 'Search headphones', 'Order status ORD123', or 'FAQ'."

# Search products with fuzzy matching
def search_products(query, num_results=3):
    if not products:
        return "Error: Product data is not available. Please try again later."

    # Preprocess query: Split into keywords and filter stopwords
    stopwords = {"a", "an", "the", "for", "with", "and"}
    keywords = [word.lower() for word in re.findall(r'\w+', query) if word.lower() not in stopwords]

    # First pass: Check for exact matches in product titles
    exact_matches = []
    for idx, product in enumerate(products):
        title = product["title"].lower()
        if any(keyword in title for keyword in keywords):
            exact_matches.append((idx, product["title"]))

    # Second pass: Fuzzy match if no exact matches
    if not exact_matches:
        product_titles = [(idx, p["title"]) for idx, p in enumerate(products)]
        matches = process.extract(
            query, 
            product_titles,
            processor=lambda x: x[1].lower(),
            scorer=fuzz.token_sort_ratio,  # Better for keyword order flexibility
            limit=None
        )
        filtered_matches = [m for m in matches if m[1] >= 70]
    else:
        # Prioritize exact matches
        filtered_matches = [((idx, title), 100) for idx, title in exact_matches]

    # Debug output
    print(f"\n🔍 Search Query: '{query}'")
    print("Filtered Matches:", [(products[m[0][0]]["title"], m[1]) for m in filtered_matches[:3]])

    if filtered_matches:
        # Sort by score descending, then alphabetical
        filtered_matches.sort(key=lambda x: (-x[1], x[0][1]))
        
        results = []
        for match in filtered_matches[:num_results]:
            product = products[match[0][0]]
            results.append(f"{product['title']} - ${product['price']}")
        return f"Found products:\n" + "\n".join(results)
    else:
        return "No products found. Try different keywords!"

# Check order status
def check_order_status(order_id):
    order = orders.get(order_id)
    if order:
        return f"Order {order_id}: {order['status']} (Last update: {order['date']})"
    else:
        return f"Order {order_id} not found. Check your order ID or contact support."

# API endpoint for chatbot
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '').strip()
    if not user_message:
        return jsonify({'response': "Please enter a message!"})
    bot_response = process_message(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)