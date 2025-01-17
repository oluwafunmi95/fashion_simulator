from flask import Flask, render_template

app = Flask(__name__)

# Sample outfit data
outfits = [
    {"name": "Red Dress", "image": "static/images/red-dress.png"},
    {"name": "Blue Jeans", "image": "static/images/blue-jeans.png"},
    {"name": "Green Shirt", "image": "static/images/green-shirt.png"},
]

@app.route("/")
def home():
    return render_template("index.html", outfits=outfits)

if __name__ == "__main__":
    app.run(debug=True)