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
    if data is None:
        return jsonify({'error': 'Invalid or missing JSON payload'}), 400
    guess_word = data.get('guess', '')
    player_name = data.get('playerName', '')
    result = game_logic.check_guess(guess_word, player_name)
    return jsonify({
        'result': result,
        'score': game_logic.score,
        'playerName': player_name
    })


@app.route('/leaderboard', methods=['POST'])
def leaderboard():
    data = request.json
    if data is None:
        return jsonify({'error': 'Invalid or missing JSON payload'}), 400

    top_scores = game_logic.get_top_scores()
    player_name = data.get('playerName', '')
    print("player name is " + str(player_name))
    return jsonify({
        'leaderboard': top_scores,
        'rank': game_logic.get_player_rank(player_name) or "Not ranked"
    })


@app.route('/reset', methods=['POST'])
def reset():
    game_logic.reset_word()
    return jsonify({'message': 'New word selected!'})


@app.route('/clue', methods=['POST'])
def clue():
    data = request.json
    player_name = data.get('playerName', '')
    game_clue = game_logic.show_clue()
    return jsonify({
        'clue': game_clue,
        'score': game_logic.score,
        'playerName': player_name
    })


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port, debug=False)