from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

# Load Kenyan product dataset
with open('kenya_products.json', 'r') as f:
    products = json.load(f)

# Mock orders
orders = {
    "ORD123": {"status": "Delivered", "date": "2023-12-15"},
    "ORD456": {"status": "Shipped", "date": "2023-12-20"}
}

# Chatbot logic
def process_message(message):
    message = message.lower()

    # Rule-based responses
    if "order" in message and "status" in message:
        order_id = message.split()[-1].upper()
        return check_order_status(order_id)
    elif "search" in message or "find" in message:
        query = message.replace("search", "").replace("find", "").strip()
        return search_products(query)
    elif "faq" in message or "help" in message:
        return get_faq()
    else:
        return "Sorry, I didn't understand! Try: 'Search headphones', 'Order status ORD123', or 'FAQ'."

# Check order status
def check_order_status(order_id):
    order = orders.get(order_id)
    if order:
        return f"Order {order_id}: {order['status']} (Last update: {order['date']})"
    else:
        return f"Order {order_id} not found. Check your order ID!"

# Search products
def search_products(query):
    results = [p for p in products if query in p["name"].lower()]
    if results:
        products_list = "\n".join([f"{p['name']} - KES {p['price']}" for p in results])
        return f"Found products:\n{products_list}"
    else:
        return "No products found. Try different keywords!"

# Get FAQ
def get_faq():
    return """FAQ:
1. Returns: 30-day policy
2. Shipping: 3-5 days
Email support@example.com for more help!"""

# API endpoint for chatbot
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    bot_response = process_message(user_message)
    return jsonify({'response': bot_response})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)