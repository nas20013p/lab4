from flask import Flask, request, jsonify

app = Flask(__name__)

# A simple in-memory store for valid tokens (for demonstration purposes)
valid_tokens = {"nazmus.sakib@uconn.edu": "f99aa8b8573062e9802f4fc0807ae1cb"}

@app.route("/")
def hello():
    return " you called \n"

@app.route("/login", methods=['POST'])
def login():
    token_id = request.form.get('token_id')
    token = request.form.get('token')
    if token_id and token and valid_tokens.get(token_id, None) == token:
        return jsonify({"message": "Login successful", "user": token_id}), 200
    else:
        return jsonify({"error": "Invalid token_id or token"}), 401

# @app.route("/echo", methods=['POST'])
# def echo():
#     token = request.form.get('token')
#     if token in valid_tokens:
#         return "You said: " + request.form['text']
#     else:
#         return jsonify({"error": "Unauthorized"}), 401

if __name__ == "__main__":
    app.run(host='0.0.0.0')
