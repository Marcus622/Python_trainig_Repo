from flask import Flask

app = Flask(__name__) # Die app dient dazu, verschiedene vorab definierte Anfragen über einen vorbestimmten Port zu leiten. In unserem Fall Port 6060.
# Über diese Schnittstelle greifen Programme auf bestimmte Funktionen oder Daten zu, ohne dass diesen der interne Code bekannt sein muss.


# GET route
@app.route("/") # Wenn die Route / aufgerufen wird, gelangt man auf die Startseite.
def home():
    return "Hello, World! This is a simple API running on Mac."


@app.route("/test")
def test_func():
    return "Test!!!"


@app.route("/max")
def max_func():
    return "MAX!!!"

@app.route("/Marcus")
def marcus_func():
    return "Marcus!!!"

@app.route("/info")
def info_func():
    return "Please call for more informations."

@app.route("/team")
def team_func():
    return "Kontaktieren Sie gerne unser Team."

@app.route("/hilfe")
def hilfe_func():
    return "call us for help."

@app.route("/contact")
def contact_func():
    return "Nehmen Sie Kontakt mit unserem Support auf." 

# Run the app
if __name__ == "__main__":
    # Use a custom port (e.g., 8080) and bind to all interfaces
    app.run(debug=True, host="0.0.0.0", port=6060) # Die app.run(port:6060) wird verwendet, um eine Schnittstelle für diese Anfragen festzulegen.
