from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def index():
	return "Hello, Devops! 🎯 this is the new and updated version with the help of github actions!!!", 200

@app.get("/health")
def health():
	return jsonify(status="ok", service="flask-app"), 200

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
