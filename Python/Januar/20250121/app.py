from flask import Flask, jsonify, request
from users import users

app = Flask(__name__)

# Route 1: /user/<int:id>
@app.route("/user/<int:id>", methods=["GET"])
def get_user(id):
    user = next((user for user in users if user["id"] == id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404
    

# Route 2: /login/<id>
@app.route("/login/<int:id>", methods=["GET"])
def login_user(id):
    user = next((user for user in users if user["id"] == id), None)
    if user:
        return jsonify({"message": f"User {user['name']} successfully logged in!"}) #return jsonify({"message": f"User {user["name"]} successfully logged in!"})

    return jsonify({"error": "Invalid user ID"}), 404


# Route 3: /search?name=<name>
@app.route("/search", methods=["GET"])
def search_user():
    name = request.args.get("name", "").strip()
    
    user = next((user for user in users if user["name"].lower() == name.lower()), None)
    if user:
        return jsonify({"message": f"Found user: {user['name']}"})
    return jsonify({"error": f"No user found with name: {name}"}), 404

if __name__ == "__main__":
    app.run(port=6060, debug=True)