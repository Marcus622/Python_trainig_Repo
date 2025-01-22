users = [
{"id": 1, "name": "Alice", "email": "alice@example.com" },
{"id": 2, "name": "Bob", "email": "bob@example.com"},
{"id": 3, "name": "Charlie", "email": "charlie@example.com"}
]

from flask import Flask, request

app = Flask(__name__)

@app.route("/users", methods=["GET"])
def home():
    return "Welcome to our users api"


@app.route("/users/<int:id>", methods=["GET"])
def get_user_by_id(user_id):
    final_user = None

    for u in users:
        if u ["id"] == user_id:
            final_user = u

        if final_user == None:
            return "User could not be found"
        
        return f"The user is {final_user}"
    
if __name__ == "__main__":
    app.run(debug=True, port=6060)