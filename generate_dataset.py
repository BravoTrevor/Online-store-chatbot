from faker import Faker
import json
import random

fake = Faker('en_US')  # Use en_US as fallback

# Kenyan customizations
swahili_words = {
    "Electronics": ["Redio", "Simu", "Televisheni", "Laptop", "Rada"],
    "Fashion": ["Viatu", "Kaniki", "Kitenge", "Kofia", "Shanga"],
    "Home & Kitchen": ["Sufuria", "Meza", "Kikombe", "Bati", "Jiko"],
    "Groceries": ["Kahawa", "Unga", "Mkate", "Chai", "Pilipili"]
}

# Manually define Kenyan brands
kenyan_brands = ["Safaricom", "Kiondo", "Dormans", "Bidco", "Brookside", "Nakumatt", "Java House"]


def generate_product(id):
    category = random.choice(list(swahili_words.keys()))
    sw_word = random.choice(swahili_words[category])

    # FIX: Replace fake.company() with a Kenyan brand
    name = f"{random.choice(kenyan_brands)} {sw_word} {fake.word().capitalize()}"

    # Generate ratings and reviews
    reviews = []
    for _ in range(random.randint(5, 20)):
        reviews.append({
            "user": fake.name(),
            "stars": random.randint(1, 5),
            "comment": fake.sentence()
        })

    # Generate variants
    variants = []
    for i in range(random.randint(1, 3)):
        variants.append({
            "id": f"{id}{chr(97 + i)}",  # 1a, 1b, 1c, etc.
            "color": fake.color_name(),
            "price_diff": random.choice([0, 500, 1000]),
            "image": f"https://source.unsplash.com/800x600/?{sw_word}-{id}-{i}"
        })

    return {
        "id": id,
        "name": name,
        "category": category,
        "price": random.randint(500, 30000),
        "currency": "KES",
        "brand": random.choice(kenyan_brands),  # Use Kenyan brands here too
        "description": fake.paragraph() + " " + fake.sentence(),
        "rating": {
            "average": round(random.uniform(3.5, 5.0), 1),
            "count": len(reviews),
            "reviews": reviews
        },
        "images": [
            f"https://source.unsplash.com/800x600/?{category.replace(' ', '-')}-{id}",
            f"https://source.unsplash.com/800x600/?{sw_word}-{id}"
        ],
        "variants": variants
    }


# Generate 50 products
products = [generate_product(i + 1) for i in range(50)]

# Save to JSON
with open('kenya_products.json', 'w') as f:
    json.dump(products, f, indent=2)