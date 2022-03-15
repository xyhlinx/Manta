## create your own venv
```commandline
python3 -m venv myvenv
```
## installation
```commandline
source ./myvenv/bin/activate
pip install -r requirements.txt
./manage.py makemigrations
./manage.py migrate
```
### run the app
```commandline
./manage.py runserver
```