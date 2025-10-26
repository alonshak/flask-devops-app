from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    # מחזיר את עמוד הפורטפוליו
    return render_template("index.html")

@app.get("/health")
def health():
    # מאפשר לבדוק שהאפליקציה פעילה
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
