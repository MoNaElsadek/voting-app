from flask import Flask, render_template, request
import redis

app = Flask(__name__)

# Connect to Redis
redis_client = redis.Redis(host='redis', port=6379)

@app.route('/')
def home():
    votes = {
        "Option 1": int(redis_client.get("option1") or 0),
        "Option 2": int(redis_client.get("option2") or 0)
    }
    return render_template('index.html', votes=votes)

@app.route('/vote', methods=['POST'])
def vote():
    option = request.form.get('option')
    if option == 'Option 1':
        redis_client.incr("option1")
    elif option == 'Option 2':
        redis_client.incr("option2")
    return home()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


