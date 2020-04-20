# 36 Music Album API
## How to run my app
1. Clone the app to your computer.
2. Open terminal or cmd  and go to file location where project cloned.
3. Use the requirements file to get all dependencies.
4. Run `pip install -r requirements.txt`
5. Run `python manage.py migrate` to create all models.
6. Run `python manage.py download_from_api key secret` to download data from api u will need the key and secret as arguments.
7. Run `python manage.py createsuperuser` to create super user.
8. Run `python manage.py runserver` to runserver.
9. Click on `http://127.0.0.1:8000/` to visit the app on browser.
