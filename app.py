from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    print(f"📨 Notifying user {data['username']} at {data['email']}")
    return jsonify({"status": "notified"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
