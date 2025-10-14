from flask import Flask
app = Flask(__name__)
import os
API_KEY = os.getenv("API_KEY")

@app.route("/")
def home():
    return "Bonjour, Caplogy !"

if __name__ == "__main__":
    app.run(debug=True)