from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Sample outfit data
outfits = [
    {"name": "Red Dress", "image": "static/images/red-dress.png"},
    {"name": "Blue Dress", "image": "static/images/blue-dress.png"},
    {"name": "Yellow Dress", "image": "static/images/yellow-dress.png"},
]

@app.route("/")
def home():
    return render_template("index.html", outfits=outfits)

@app.route("/try-on", methods=["POST"])
def try_on():
    data = request.json
    selected_outfit = data.get("outfit")
    return jsonify({"message": "Outfit selected!", "outfit": selected_outfit})

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5001)))