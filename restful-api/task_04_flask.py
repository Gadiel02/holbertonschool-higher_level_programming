from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Route for the root URL
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# Route to get status
@app.route("/status")
def status():
    return "OK"

# Route to fetch all usernames
@app.route("/data")
def get_usernames():
    usernames = list(users.keys())  # Get the list of all usernames
    return jsonify(usernames)

# Route to fetch user data by username
@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Route to add a new user (POST request)
@app.route("/add_user", methods=["POST"])
def add_user():
    user_data = request.json
    username = user_data.get("username")
    
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    # Add the new user to the dictionary
    users[username] = {
        "username": username,
        "name": user_data.get("name"),
        "age": user_data.get("age"),
        "city": user_data.get("city")
    }
    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__":
    app.run(debug=True)
