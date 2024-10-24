from flask import Flask, request

app = Flask(__name__)

# HTML template for the starting page, where the user imagines a number
HTML_START = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guess The Number</title>
</head>
<body>
<h1>Imagine number between 0 and 1000</h1>
<form action="" method="POST">
    <input type="hidden" name="min" value="{}"></input>
    <input type="hidden" name="max" value="{}"></input>
    <input type="submit" value="OK">
</form>
</body>
</html>
"""

# HTML template for when the program makes a guess
HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guess The Number</title>
</head>
<body>
<h1>It is number {guess}</h1>
<form action="" method="POST">
    <input type="submit" name="user_answer" value="too big">
    <input type="submit" name="user_answer" value="too small">
    <input type="submit" name="user_answer" value="you won">
    <input type="hidden" name="min" value="{min}">
    <input type="hidden" name="max" value="{max}">
    <input type="hidden" name="guess" value="{guess}">
</form>
</body>
</html>
"""

# HTML template for the winning page, where the program guesses correctly
HTML_WIN ="""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guess The Number</title>
</head>
<body>
<h1>Hurra! I guessed! Your number is {guess}</h1>
</body>
</html>
"""

# Route that handles the main game logic
@app.route('/', methods=['GET', 'POST'])
def guess_number():
    if request.method == 'GET':
        # On GET request, display the starting page with the range 0 to 1000
        return HTML_START.format(0, 1000)
    else:
        # Retrieve form values
        min_number = int(request.form.get('min'))  # Min number provided by the form
        max_number = int(request.form.get('max'))  # Max number provided by the form
        user_answer = (request.form.get('user_answer'))  # User's response to the guess
        guess = int(request.form.get('guess', 500))  # Default guess is 500

        # Adjust the guess based on the user's input
        if user_answer == 'too big':
            max_number = guess  # If guess is too big, adjust the max number
        elif user_answer == 'too small':
            min_number = guess  # If guess is too small, adjust the min number
        elif user_answer == 'you won':
            # If the user confirms the guess is correct, show the win page
            return HTML_WIN.format(guess=guess)

        # Calculate a new guess using binary search logic
        guess = (max_number - min_number) // 2 + min_number
        return HTML.format(guess=guess, min=min_number, max=max_number)

# Start the Flask app
if __name__ == '__main__':
    app.run()