import random
##ABHEEk akira todo:
## 1. reset button fix
## 2. add colors (green, yellow, gray). DONE
## 3. gameover when six entered,a nd show answer
## 4. eror handle when size is not 5

## For later
## 5. accept input of number of wordle letters from user, (4         or 5 or 6)
## 6. valid word or not (api call)
## 7.get any random word from api call.(internT)

# Word list
WORDS = ['apple', 'grape', 'chair', 'table', 'plant']

# Choose a target word at random
target_word = random.choice(WORDS)
count = 0

def reset_word():
    global target_word, count
    target_word = random.choice(WORDS)
    count = 0
    return target_word


def check_guess(guess):
    """Compare the guess to the target word and return color-coded result."""
    result = []
    guess = guess.lower()
    global count
    count += 1
    for i, letter in enumerate(guess):
        if letter == target_word[i]:
            result.append(f'<span class="letter correct">{letter.upper()}</span>')
        elif letter in target_word:
            result.append(f'<span class="letter partial">{letter.upper()}</span>')
        else:
            result.append(f'<span class="letter incorrect">{letter.upper()}</span>')
    return result
