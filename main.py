from flask import Flask, request, jsonify, render_template
import game_logic  # import kids' logic
import os

os.environ['FLASK_APP'] = 'main.py'
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/wordle')
def wordle():
    return render_template('wordle.html')


@app.route('/guess', methods=['POST'])
def guess():
    data = request.json
    guess_word = data.get('guess', '')
    result = game_logic.check_guess(guess_word)
    return jsonify({'result': result})


@app.route('/reset', methods=['POST'])
def reset():
    game_logic.reset_word()
    return jsonify({'message': 'New word selected!'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)