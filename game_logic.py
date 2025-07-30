import random
import json
import os

##ABHEEk akira todo:
## 1. reset button fix - DONE
## 2. add colors (green, yellow, gray). DONE
## 3. gameover when six entered,a nd show answer -DONE
## 4. eror handle when size is not 5 -DONE
## 5. add all the entries into line by line , with letter backgroudn color - DONE

## For later
## 5. accept input of number of wordle letters from user, (4         or 5 or 6)
## 6. valid word or not (api call)
## 7.get any random word from api call.(internT)

# Word list
WORDS = {
    "apple": "Something you eat and the brand of a laptop",
    "grape": "A purple fruit that sometimes is green ",
    'chair': 'Something you sit on',
    'table': 'Something that you can put things on while you are sitting ',
    'plant': 'related to greenery',
    'house': 'What you live in',
    'water': 'Something you drink',
    'phone': 'A device you talk through',
    'clock': 'Something which tells the time',
    'paper': 'Something you write on',
    'pizza': 'Something you eat which has cheese',
    'bread': 'Something which is used to make sandwhiches',
    'juice': 'Something you drink which has natural flavor(fruits)',
    'sugar': 'A ingriedient for sweets(it makes things              sweet)',
    'sweet': 'Something that usually has a lot of sugar',
    'sauce': 'Something which you may use for     dressing',
    'spoon': 'A utensile to eat',
    'knife': 'A utensile to cut',
    'plate': 'Something you eat on',
    'glass': 'Something you drink in',
}
# Choose a target word at random
words_keys = list(WORDS.keys())
target_word = random.choice(words_keys)

count = 0
result = []
score = 0

# Leaderboard file
LEADERBOARD_FILE = 'leaderboard.json'


def load_leaderboard():
    """Load leaderboard from file"""
    if os.path.exists(LEADERBOARD_FILE):
        try:
            with open(LEADERBOARD_FILE, 'r') as f:
                return json.load(f)
        except:
            return []
    return []


def get_player_rank(player_name):
    print("inside get_player_rank" + player_name)
    """Get the rank of a specific player"""
    leaderboard = load_leaderboard()

    # Sort by score (highest first) to ensure correct ranking
    leaderboard.sort(key=lambda x: x['score'], reverse=True)

    # Find player and return their rank (1-based)
    for i, player in enumerate(leaderboard):
        if player['name'] == player_name:
            return i + 1  # +1 because rank starts at 1, not 0

    # Player not found
    return None


def save_leaderboard(leaderboard):
    """Save leaderboard to file"""
    with open(LEADERBOARD_FILE, 'w') as f:
        json.dump(leaderboard, f)


def update_leaderboard(player_name, player_score):
    """Update leaderboard with new score"""
    leaderboard = load_leaderboard()

    player_found = False
    for player in leaderboard:
        if player['name'] == player_name:
            player['score'] = player['score'] + player_score
            player_found = True
            break

    if not player_found:
        # Add new score
        leaderboard.append({'name': player_name, 'score': player_score})

    # Sort by score (highest first)
    leaderboard.sort(key=lambda x: x['score'], reverse=True)

    # Keep only top 1000
    leaderboard = leaderboard[:1000]

    save_leaderboard(leaderboard)
    return leaderboard


def get_top_scores():
    """Get top 10 scores for display"""
    leaderboard = load_leaderboard()
    return leaderboard[:10]  # Return only top 10 scores


def reset_word():
    global target_word, count, score
    target_word = random.choice(list(WORDS.keys()))
    count = 0
    return target_word


# game_logic.py
def show_clue():
    global score
    print("inside clue target word is" + target_word)
    score = score - 100  # Deduct 100 points for using a clue
    return WORDS[target_word]


def check_guess(guess, player_name=''):
    print("inside guess target word is" + target_word)
    """Compare the guess to the target word and return color-coded result."""
    global count
    global result
    global score

    print("target world is" + target_word)
    if count == 0:
        score = 0  # Initialize score for new game
        print("New game started")
        result = []
    guess = guess.lower()
    count += 1

    # Validate guess length
    if len(guess) != len(target_word):
        result.append(
            f'<span class="letter unanswered">Please enter a {len(target_word)}-letter word!</span>'
        )
        count -= 1  # Don't count invalid guesses
        return result

    # Game won if guess is correct
    if guess == target_word:
        result.append(
            f'<span class="letter answered">YOU WON! The word was {target_word}) </span>'
        )
        result.append(
            f'<span class="letter answered">Level 2️⃣ COMING SOON :)</span>')
        score = score + 300 - (count - 1) * 50
        result.append(
            f'<span class="letter answered">Your current score is {score}</span>'
        )

        # Update leaderboard if player name is provided
        if player_name:
            update_leaderboard(player_name, score)

        reset_word()
        return result


# Game over if 5 guesses are made
    if count >= 5:
        result.append(
            f'<span class="letter unanswered">GAME OVER! The word was {target_word}</span>'
        )
        reset_word()
        return result

    for i, letter in enumerate(guess):
        if letter == target_word[i]:
            result.append(
                f'<span class="letter correct">{letter.upper()}</span>')
        elif letter in target_word:
            result.append(
                f'<span class="letter partial">{letter.upper()}</span>')
        else:
            result.append(
                f'<span class="letter incorrect">{letter.upper()}</span>')

    result.append('<br>')
    return result
