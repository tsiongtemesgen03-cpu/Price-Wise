from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return """
    <h1>Price-Wise App ✅</h1>
    <p>Your app is successfully deployed on Railway 🚀</p>
    """

# Simple test API
@app.route("/api/test")
def test():
    return jsonify({"message": "API is working!"})

# Example pricing endpoint (demo mode)
@app.route("/api/price", methods=["POST"])
def get_price():
    data = request.json

    bedrooms = data.get("bedrooms", 1)
    accommodates = data.get("accommodates", 2)

    # Simple fake pricing logic (since model removed)
    price = 100 + (bedrooms * 50) + (accommodates * 10)

    return jsonify({
        "recommended_price": price,
        "note": "Demo mode (no ML model loaded)"
    })

# Run app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)