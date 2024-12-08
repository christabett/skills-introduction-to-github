
from flask import Flask, jsonify, request

app = Flask(__name__)
from flask_cors import CORS
CORS(app)

@app.route('/')
def home():
    return "Welcome to the Flask Backend! The server is running."


# In-memory data for quick prototyping (mock database)
users = {"influencers": [], "merchants": []}
campaigns = []

# Basic User Registration
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    user_type = data.get("type")  # "influencer" or "merchant"
    user_data = {
        "name": data.get("name"),
        "location": data.get("location"),
        "niche": data.get("niche") if user_type == "influencer" else data.get("industry"),
        "email": data.get("email"),
    }
    if user_type == "influencer":
        users["influencers"].append(user_data)
    elif user_type == "merchant":
        users["merchants"].append(user_data)
    else:
        return jsonify({"error": "Invalid user type"}), 400
    return jsonify({"message": f"{user_type.capitalize()} registered successfully!", "data": user_data}), 201

# Basic Campaign Management
@app.route('/campaigns', methods=['GET', 'POST'])
def handle_campaigns():
    if request.method == 'POST':
        data = request.json
        campaign = {
            "id": len(campaigns) + 1,
            "merchant": data.get("merchant"),
            "title": data.get("title"),
            "description": data.get("description"),
            "requirements": data.get("requirements"),
            "location": data.get("location"),
            "credits": data.get("credits"),
        }
        campaigns.append(campaign)
        return jsonify({"message": "Campaign created successfully!", "campaign": campaign}), 201
    elif request.method == 'GET':
        return jsonify({"campaigns": campaigns}), 200

# Running the app
if __name__ == "__main__":
    app.run(debug=True)
