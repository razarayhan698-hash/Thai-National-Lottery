from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

lottery_data = {
    "123456": "Winner - $500",
    "654321": "Better luck next time",
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    token = request.json.get('token')
    result = lottery_data.get(token, "Result Not Found")
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run()
