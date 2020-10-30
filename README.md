# textSummarizer
This is the backend for a Text Summarizer built with Django.  
To run this on windows -
```bash
python3 -m venv env
.\env\Scripts\activate
```
To run this on Linux - 
```
python -m venv env
source env/bin/activate
```
Then install the requirements.
```
pip install -r requirements.txt
```
Then make the migrations for Django.
```
python manage.py makemigrations
python manage.py migrate
```
Then create a super user so that you can access the admin page to see the models.
```
python manage.py createsuperuser
```
Then start the server.
```
python manage.py runserver
```
Then head to 127.0.0.1:8000/home to enter the title of the artile, for example enter "Wikipedia".  
Then in 127.0.0.1:8000/admin after logging in and going to the "Article" model, you can see the data entered by you.
