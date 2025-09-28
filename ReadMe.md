django-admin startproject matrix_game
cd matrix_game
python manage.py startapp game
<!-- Click cells to select/deselect numbers.

Check Your Path button validates if the selected numbers sum to the target.

Shows correct or wrong message.

Backend paths are still displayed in text (optional hints).

Works with your existing Django backend. -->

python manage.py migrate
python manage.py makemigration

python manage.py runserver
# Game - 2
python manage.py startapp tic_tac_toe
<!-- Board Storage: Stored in request.session as a 3x3 list.

Move Handling: Updates the board when a user clicks a cell.

Player Switch: Alternates between "X" and "O".

Winner Check: Checks rows, columns, and diagonals after each move.

Reset: Can reset the game via ?reset=1 in the URL. -->

# Game 3
python manage.py startapp math_game
