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
# Games
