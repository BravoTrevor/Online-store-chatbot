# Online-store-chatbot
AI-powered chatbot for an African e-commerce platform (inspired by Jumia/Kilimall). This chatbot will:

Help users search for products.

Provide product recommendations.

Answer FAQs (e.g., shipping, returns).

Track orders (mock data).

This is a portfolio project to showcase your AI and full-stack development skills, with a focus on African markets.

Sections of the Project
1. Kenyan Product Dataset
What it is: A realistic mock catalog of products sold in Kenya.

Details:

50-100 products with names, prices, descriptions, ratings, reviews, and images.

Includes Swahili-English mix for authenticity.

Products have variants (e.g., colors, sizes) and mock ratings/reviews.

How it fits: This dataset is the brain of the chatbot. It’s where the chatbot gets product info to answer user queries.

2. Chatbot Backend (Python)
What it is: The logic that powers the chatbot.

Details:

Built with Flask (a Python web framework).

Handles user messages, processes them, and generates responses.

Uses rule-based logic (e.g., if the user says “search,” it looks up products).

Can be extended with NLP (e.g., to understand Swahili/English mix).

How it fits: The backend is the engine that connects the user interface (UI) to the product dataset.

3. Chatbot Frontend (Web UI)
What it is: The user interface where users interact with the chatbot.

Details:

A floating chat button on the bottom-right of the webpage.

A chat window with:

Message bubbles (user messages on the right, bot replies on the left).

A typing box and Send button.

Built with HTML/CSS/JavaScript.

How it fits: This is the face of the chatbot. Users type here, and the chatbot’s replies appear here.

4. Integration (Frontend + Backend)
What it is: The connection between the web UI and the Python backend.

Details:

The frontend sends user messages to the backend via API calls (using fetch in JavaScript).

The backend processes the message, queries the dataset, and sends a reply back to the frontend.

The frontend displays the reply in the chat window.

How it fits: This is the bridge that makes the chatbot work end-to-end.

5. Deployment
What it is: Making the chatbot accessible online for your portfolio.

Details:

The frontend will be hosted on GitHub Pages (free and easy).

The backend will be hosted on Heroku or Render (free tiers available).

The dataset will be stored as a JSON file, either in the backend or on GitHub.

How it fits: Deployment makes your chatbot live so recruiters can interact with it.

How Everything Fits Together
User Interaction:

A user visits your GitHub Pages site and sees the chatbot button.

They type a message (e.g., “Search for phones”).

Frontend:

The JavaScript code sends the message to the Python backend via an API call.

Backend:

The Flask app receives the message, processes it (e.g., searches the dataset), and generates a reply.

The reply is sent back to the frontend.

Frontend (Again):

The reply is displayed in the chat window as a message bubble.

Dataset:

The backend queries the Kenyan product dataset to find relevant products or answers.
