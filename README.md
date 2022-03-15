## create your own venv
```commandline
python3 -m venv myvenv
```
## installation
```commandline
pip install -r requirements.txt
source ./myvenv/bin/activate
./manage.py makemigrations
./manage.py migrate
```
### run the app
```commandline
./manage.py runserver
```