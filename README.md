**HeyrronScramble**

HeyrronScramble is a fun and interactive web-based app designed to improve students' vocabulary and critical thinking skills. The app is particularly useful for students preparing for the SAT exam, as it helps them enhance their English vocabulary while solving engaging word scramble puzzles.

The app has been successfully tested among students, resulting in a notable improvement in SAT vocabulary, with users increasing their overall SAT English scores by up to 100 points.


**Features**
- **Word Scrambling**: Randomly scrambles letters of words to create puzzles.
- **SAT-Level Vocabulary**: Uses a database of words commonly encountered in SAT exams.
- **Interactive Scoring**: Tracks user score based on correct answers and the number of attempts.
- **Difficulty Levels**: Users can switch between two difficulty levels—*Standard* and *Advanced*.
- **Feedback Mechanism**: Provides instant feedback on each answer, including the word's meaning when correct.
- **Mobile Friendly**: Fully responsive design for use on mobile devices.

**Technologies**
- **Flask**: A lightweight WSGI web application framework.
- **HTML/CSS**: For creating the front-end interface.
- **JavaScript**: To handle user interactions dynamically.
- **Python**: Backend logic and word processing.

**Installation**

1. **Clone the repository**:
    ```bash
    git clone https://github.com/heyrron/heyrronscramble.git
    cd heyrronscramble
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the app**:
    ```bash
    python app.py
    ```

5. **Access the app**:
    Open your browser and navigate to `http://127.0.0.1:5000/`.

**Usage**

1. Start the app by running `python app.py` in your terminal.
2. Upon loading the app in your browser, you will be presented with a scrambled word and the definition of the correct word.
3. Guess the correct word by entering it into the input field. You will receive immediate feedback on whether your guess is correct or incorrect.
4. After 3 incorrect attempts, the correct word will be revealed, and a new puzzle will be generated automatically.

**File Structure**
```
heyrronscramble/
│
├── static/
│   ├── css/
│   │   └── challenge.css            # Styling for the app
│
├── templates/
│   ├── challenge.html            # Main game interface
│
├── words_standard.txt            # Word list for 'Standard' difficulty
├── words_advanced.txt            # Word list for 'Advanced' difficulty
├── app.py                        # Main Flask application
├── requirements.txt              # List of Python dependencies
└── README.md                     # This file
```

**How It Works**

1. **Word Selection**: The app selects a random word from a predefined word list (`words_standard.txt` or `words_advanced.txt`).
2. **Scrambling**: The letters of the selected word are shuffled to create a scramble puzzle.
3. **Session Tracking**: The app keeps track of the user's score, the number of attempts, and the difficulty level.
4. **User Interaction**: The user guesses the word, receives feedback, and continues to the next puzzle.
5. **Difficulty**: Users can switch between standard and advanced word lists.

**Contributing**

Contributions are welcome! Please open an issue or submit a pull request with any suggestions or improvements.
