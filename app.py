from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Sample categorized outfit data
outfits = {
    "tops": [
        {"name": "Top 1", "image": "static/images/top1.png"},
        {"name": "Top 2", "image": "static/images/top2.png"}
    ],
    "bottoms": [
        {"name": "Bottom 1", "image": "static/images/bottom1.png"},
        {"name": "Bottom 2", "image": "static/images/bottom2.png"}
    ],
    "dresses": [
        {"name": "Red Dress", "image": "static/images/red-dress.png"},
        {"name": "Blue Dress", "image": "static/images/blue-dress.png"},
        {"name": "Yellow Dress", "image": "static/images/yellow-dress.png"}
    ],
    "accessories": [
        {"name": "Hat 1", "image": "static/images/hat1.png"},
        {"name": "Hat 2", "image": "static/images/hat2.png"}
    ]
}

@app.route("/")
def home():
    # Pass the categorized outfits to the template
    return render_template("index.html", outfits=outfits)

@app.route("/try-on", methods=["POST"])
def try_on():
    data = request.json
    category = data.get("category")
    outfit_name = data.get("outfit")
    
    if category in outfits:
        selected_outfit = next((o for o in outfits[category] if o["name"] == outfit_name), None)
        if selected_outfit:
            return jsonify({"message": "Outfit selected!", "outfit": selected_outfit})
    
    return jsonify({"message": "Outfit not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5001)))
