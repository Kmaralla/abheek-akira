import random

# Word list
WORDS = ['apple', 'grape', 'chair', 'table', 'plant']

# Choose a target word at random
target_word = random.choice(WORDS)


def reset_word():
    """Pick a new target word randomly."""
    global target_word
    target_word = random.choice(WORDS)
    return target_word


def check_guess(guess):
    """Compare the guess to the target word and return color-coded result."""
    result = []
    guess = guess.lower()

    for i, letter in enumerate(guess):
        if letter == target_word[i]:
            result.append("green")
        elif letter in target_word:
            result.append("yellow")
        else:
            result.append("gray")
    return result
