import random
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
WORDS = ['apple', 'grape', 'chair', 'table', 'plant']
SIX_WORDS = ['apple', 'grape', 'chair', 'table', 'plant']

# Choose a target word at random
target_word = random.choice(WORDS)
count = 0
result = []


def reset_word():
    global target_word, count
    target_word = random.choice(WORDS)
    count = 0
    return target_word


def check_guess(guess):
    """Compare the guess to the target word and return color-coded result."""
    global count
    global result
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
