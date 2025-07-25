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
WORDS = [
    'apple', 'grape', 'chair', 'table', 'plant', 'house', 'water', 'phone',
    'clock', 'paper', 'pizza', 'bread', 'juice', 'sugar', 'sweet', 'sauce',
    'spoon', 'knife', 'fork', 'plate', 'glass', 'bowl', 'fork'
]

# Choose a target word at random
target_word = random.choice(WORDS)
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

def save_leaderboard(leaderboard):
    """Save leaderboard to file"""
    with open(LEADERBOARD_FILE, 'w') as f:
        json.dump(leaderboard, f)

def update_leaderboard(player_name, player_score):
    """Update leaderboard with new score"""
    leaderboard = load_leaderboard()
    
    # Add new score
    leaderboard.append({'name': player_name, 'score': player_score})
    
    # Sort by score (highest first)
    leaderboard.sort(key=lambda x: x['score'], reverse=True)
    
    # Keep only top 5
    leaderboard = leaderboard[:5]
    
    save_leaderboard(leaderboard)
    return leaderboard

def get_top_scores():
    """Get top 5 scores for display"""
    return load_leaderboard()


def reset_word():
    global target_word, count
    target_word = random.choice(WORDS)
    count = 0
    return target_word


def check_guess(guess, player_name=''):
    """Compare the guess to the target word and return color-coded result."""
    global count
    global result
    global score

    if count == 0:
        print("New game started")
        result = []
    guess = guess.lower()
    count += 1

    # Game won if guess is correct
    if guess == target_word:
        result.append(
            f'<span class="letter answered">YOU WON! The word was {target_word}</span>'
        )
        score = 300 - (count - 1) * 50
        result.append(
            f'<span class="letter answered">Your score is {score}</span>')

        # Update leaderboard if player name is provided
        if player_name:
            update_leaderboard(player_name, score)

        reset_word()
        return result


# Game over if 6 guesses are made
    if count >= 6:
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
