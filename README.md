
# 🎯 Abheek & Akira's Fun Zone 

## 1. Wordle Game

A colorful and kid-friendly Wordle game built with Flask and JavaScript, designed by Abheek and Akira for fun learning!

## 🌟 Features

- **Interactive Wordle Game**: Guess 5-letter words with visual feedback
- **Color-coded Letters**: 
  - 🟢 Green: Correct letter in correct position
  - 🟡 Yellow: Correct letter in wrong position  
  - ⚫ Gray: Letter not in the word
- **Scoring System**: 
  - Start with 300 points
  - Lose 50 points per guess attempt
  - Lose 100 points for using a clue
- **Leaderboard**: Track top 10 players across all games
- **Player Rankings**: See your overall rank among all players
- **Helpful Clues**: Get hints about the word (with point penalty)
- **Responsive Design**: Works on desktop and mobile devices

## 🎮 How to Play

1. Enter your name to start playing
2. Guess a 5-letter word
3. Use the color feedback to make better guesses
4. Try to guess the word in 5 attempts or less
5. Use the clue button if you need help (costs 100 points)
6. Start a new game anytime with the reset button

## 🏆 Scoring Rules

- **First attempt win**: 300 points
- **Each guess attempt**: -50 points  
- **Using a clue**: -100 points
- **Fifth attempt win**: 100 points
- **No correct guess**: 0 points
- **Overall rank**: Sum of all your game scores

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Flask

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/abheekakira-wordle.git
cd abheekakira-wordle
```

2. Install dependencies:
```bash
pip install flask
```

3. Run the application:
```bash
python main.py
```

4. Open your browser and go to `http://localhost:3000`

## 📁 Project Structure

```
├── templates/
│   ├── home.html          # Welcome page
│   └── wordle.html        # Main game page
├── main.py                # Flask application routes
├── game_logic.py          # Game logic and scoring
├── leaderboard.json       # Persistent leaderboard storage
└── README.md             # This file
```

## 🎨 Game Screenshots

### Home Page
Welcome screen with colorful design and game selection

### Wordle Game
- Three-panel layout: Leaderboard | Game | Instructions
- Real-time scoring and ranking
- Visual letter feedback
- Player name tracking

## 🛠️ Technical Details

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Styling**: Comic Sans MS font for kid-friendly appeal
- **Data Storage**: JSON file for leaderboard persistence
- **Responsive**: CSS Flexbox layout with mobile support

## 🎯 Game Logic

The game includes a curated word list with hints:
- 20+ common 5-letter words
- Each word has an associated clue
- Random word selection for each new game
- Input validation and error handling

## 🏅 Leaderboard System

- Persistent scoring across sessions
- Top 10 player display
- Individual player ranking
- Cumulative scoring from multiple games

## 🎨 Design Features

- Gradient backgrounds with vibrant colors
- Rounded corners and smooth transitions
- Kid-friendly Comic Sans MS typography
- Responsive three-column layout
- Visual feedback for all game interactions

## 🔧 Customization

You can easily customize:
- Word list in `game_logic.py`
- Scoring values in the `check_guess()` function
- Visual styling in the HTML templates
- Add new game modes or features

## 🤝 Contributing

This is a fun project by kids for kids! Feel free to:
- Add more words to the word list
- Improve the UI/UX
- Add new game features
- Fix bugs or improve performance

## 📝 License

This project is open source and available under the MIT License.

## 👥 Authors

- **Abheek** - Game design and development
- **Akira** - Game design and development

## 🎉 Fun Facts

- Designed with kids in mind
- Colorful and engaging interface
- Educational word game that improves vocabulary
- Competitive scoring system to encourage learning

---

**Have fun playing and learning!** 🌟✨

*Made with ❤️ by Abheek and Akira*
