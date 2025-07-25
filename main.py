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
    player_name = data.get('playerName', '')
    result = game_logic.check_guess(guess_word, player_name)
    return jsonify({'result': result, 'score': game_logic.score, 'playerName': player_name})

@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    top_scores = game_logic.get_top_scores()
    return jsonify({'leaderboard': top_scores})



@app.route('/reset', methods=['POST'])
def reset():
    game_logic.reset_word()
    return jsonify({'message': 'New word selected!'})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port, debug=False)