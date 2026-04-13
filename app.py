from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/reply", methods=["POST"])
def reply():
    data = request.get_json(force=True, silent=True) or {}
    print("Incoming:", data)
    
    text = data.get("text") or data.get("message", {}).get("text", "")
    reply_text = f"You said: {text}"
    
    return jsonify({"reply": reply_text})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
