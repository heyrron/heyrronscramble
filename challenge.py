from flask import Flask, render_template, request, session, jsonify
import random
import os  # Import os to handle file paths

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Function to load words from a file
def load_words(filename):
    # Get the absolute path of the file relative to the Python script
    filepath = os.path.join(os.path.dirname(__file__), filename)
    words_dict = {}
    with open(filepath, 'r') as f:
        for line in f:
            word, meaning = line.strip().split(':')
            words_dict[word] = meaning
    return words_dict

# Function to scramble the letters of a word
def scramble_word(word):
    return ''.join(random.sample(word, len(word)))

@app.route('/')
def index():
    # Initialize session variables
    if 'score' not in session:
        session['score'] = 0
    if 'attempts' not in session:
        session['attempts'] = 0
    if 'difficulty' not in session:
        session['difficulty'] = 'standard'  # Default difficulty

    # Load words based on difficulty
    if session['difficulty'] == 'advanced':
        words_dict = load_words('words_advanced.txt')
    else:
        words_dict = load_words('words_standard.txt')

    # Initialize a new game if no word is in session
    if 'word' not in session:
        session['score'] = 0  # Reset score at the start of a new game
        session['attempts'] = 0  # Reset attempts at the start of a new game
        word = random.choice(list(words_dict.keys()))
        scrambled_word = scramble_word(word)
        session['word'] = word  # Store new word in session
        session['scrambled_word'] = scrambled_word  # Store scrambled word in session
        session['meaning'] = words_dict[word]  # Store meaning in session

    return render_template('challenge.html',
                           scrambled_word=session['scrambled_word'],
                           score=session['score'],
                           attempts=session['attempts'],
                           result='',
                           meaning=session['meaning'])

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input'].strip().lower()
    word = session.get('word').strip().lower()  # Get the current word from session

    # Load words based on difficulty
    if session['difficulty'] == 'advanced':
        words_dict = load_words('words_advanced.txt')
    else:
        words_dict = load_words('words_standard.txt')

    # Initialize result and meaning
    result = ""
    meaning = ""

    # Check if user's input is correct
    if user_input == word:
        session['score'] += 1
        result = "👌 Correct! Well done."
        meaning = f"The meaning of {word} is: {session['meaning']}"
        # Generate new word and scrambled word for the next round
        word = random.choice(list(words_dict.keys()))
        scrambled_word = scramble_word(word)
        session['word'] = word
        session['scrambled_word'] = scrambled_word
        session['meaning'] = words_dict[word]
        session['attempts'] = 0  # Reset attempts after a correct guess
    else:
        session['attempts'] += 1
        if session['attempts'] < 3:
            result = f"❌ Incorrect. You have {3 - session['attempts']} attempts left."
            meaning = ""
        else:
            result = f"❌ Incorrect. The correct word is {word}."
            meaning = f"The meaning of the word is: {session['meaning']}"
            # Generate new word and scrambled word for the next round
            word = random.choice(list(words_dict.keys()))
            scrambled_word = scramble_word(word)
            session['word'] = word
            session['scrambled_word'] = scrambled_word
            session['meaning'] = words_dict[word]
            session['attempts'] = 0  # Reset attempts after 3 incorrect attempts

    return render_template('challenge.html',
                           scrambled_word=session['scrambled_word'],
                           score=session['score'],
                           attempts=session['attempts'],
                           result=result,
                           meaning=meaning)

@app.route('/next-word')
def next_word():
    # Load words based on difficulty
    if session['difficulty'] == 'advanced':
        words_dict = load_words('words_advanced.txt')
    else:
        words_dict = load_words('words_standard.txt')

    # Only change word if attempts have run out or if the user answered correctly
    if session.get('attempts', 0) >= 3 or 'word' not in session:
        word = random.choice(list(words_dict.keys()))
        scrambled_word = scramble_word(word)
        session['word'] = word  # Store new word in session for next round
        session['scrambled_word'] = scrambled_word  # Store new scrambled word in session
        session['meaning'] = words_dict[word]  # Store new meaning in session
        session['attempts'] = 0  # Reset attempts for new word

    return jsonify({'scrambled_word': session['scrambled_word'], 'word': session['word']})

@app.route('/set-difficulty', methods=['POST'])
def set_difficulty():
    difficulty = request.form.get('difficulty')
    if difficulty in ['standard', 'advanced']:
        session['difficulty'] = difficulty
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)