import json

# Load your original dataset with UTF-8 encoding
with open('Amazon products.json', 'r', encoding='utf-8') as f:
    original_data = json.load(f)

# Extract only the necessary fields
simplified_data = []
for product in original_data:
    simplified_product = {
        "title": product.get("title", "No title"),
        "price": product.get("final_price", 0.0),
        "image": product.get("image_url", ""),
        "description": product.get("description", "No description"),
        "rating": product.get("rating", 0.0),
        "in_stock": product.get("availability", "In Stock") == "In Stock",
        "currency": product.get("currency", "USD")
    }
    simplified_data.append(simplified_product)

# Save the simplified dataset
with open('amazon_products_simple.json', 'w', encoding='utf-8') as f:
    json.dump(simplified_data, f, indent=2)

print("Simplified dataset created: amazon_products_simple.json")