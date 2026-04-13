from flask import Flask, request, jsonify
import os, json

app = Flask(__name__)

@app.route("/reply", methods=["POST"])
def reply():
    data = request.get_json(force=True, silent=True) or {}
    print("Incoming:", json.dumps(data, indent=2))

    # bot sends: {"message": "hello", "chat_id": ..., "user_id": ..., "timestamp": ...}
    text = data.get("message") or data.get("text", "")

    reply_text = f"You said: {text}"
    print("Replying:", reply_text)

    return jsonify({"reply": reply_text})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
