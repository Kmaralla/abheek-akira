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
    target_word = random.choice(WORDS)
    return target_word


def check_guess(guess):
    """Compare the guess to the target word and return color-coded result."""
    result = []
    guess = guess.lower()
    count += 1
    for i, letter in enumerate(guess):
        if letter == target_word[i]:
            result.append("🟩")
        elif letter in target_word:
            result.append("🟨")
        else:
            result.append("⬛")
    return result
