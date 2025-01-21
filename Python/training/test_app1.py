from flask import Flask

app = Flask(__name__)


# GET route
@app.route("/")
def home():
    return "Hello, World! This is a simple API running on Mac."

@app.route("/greet/<name>")
def greet(name):
    return f"Hallo {name}, willkommen  auf meiner Flask-API."


@app.route("/test")
def test_func():
    return "Test!!!"


@app.route("/max")
def max_func():
    return "MAX!!!"


@app.route("/about")
def about_func():
    return "Mein Name ist Marcus Vix und ich bin der irrsinnigen Idee verfallen, Programmieren zu lernen."

@app.route("/project")
def project_func():
    return "Dies ist der erste Versuch zur Programmierung einer Flask-API für blutige Anfänger."

@app.route("/news")
def news_func():
    return "Heute lernen wir, eine Schnittstelle für einen Port einzurichten, über die ein vordefinierter Datenverkehr laufen soll."

@app.route("/feedback")
def feedback_func():
    return "Wir freuen uns über ein positives feedback, aber auch über sachlich formulierte Kritik."

@app.route("/support")
def support_func():
    return "Bei Problemen mit ihren Anfragen kontaktieren Sie gerne unseren Support."


# Run the app
if __name__ == "__main__":
    # Use a custom port (e.g., 8080) and bind to all interfaces
    app.run(debug=True, host="0.0.0.0", port=6060)