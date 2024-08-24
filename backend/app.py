from flask import Flask, request, jsonify

app = Flask(__name__)

votes = {"option1": 0, "option2": 0}

@app.route('/vote', methods=['POST'])
def vote():
    data = request.get_json()
    option = data.get('vote')
    if option in votes:
        votes[option] += 1
        return jsonify({"message": f"Vote counted for {option}!", "votes": votes})
    return jsonify({"error": "Invalid vote option!"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)


