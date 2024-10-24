# Guess the Number Game

## Overview
- This is a simple number guessing game where the program tries to guess a number between 0 and 1000 that the user thinks of.
- The program uses binary search to minimize guesses, and the user gives feedback using "too big", "too small", or "you won".

## Features
- **Flask-based web interface**: Play the game in your browser.
- **Binary search logic**: Efficient guessing by halving the range with each guess.
- **User input feedback**: Helps guide the program to the correct guess.

## How to Run
1. **Install Flask**:
   ```bash
   pip install Flask
   
2. **Run the application**:
    ```bash
   python app.py

3. **Open in browser**: Go to http://127.0.0.1:5000/.

## Technologies

- **Python**: Used for game logic.
- **Flask**: Framework for creating the web interface.