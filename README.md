# Django Terminapplikation

To set up and start the project follow these steps:

- clone the repository.
- Use "pip install -r requirements.txt" (use pip3 if you also have python2 installed) to install the requirements to your local python. Alternatively, create a new virtual env from the requirements.txt using virtualenv.

Continue with these commands (use python3 if you also have python2 installed):    
- run "python manage.py makemigrations" and "python manage.py migrate" to create the database.
- run "python manage.py createsuperuser" to create an admin user.
- run "python manage.py runserver" to run the app with the django dev server.
- you can log in with the admin account and take a look at the app. Alternatively you can log into the django admin backend at /admin with the admin account 
and create other users. With these you can then log into the main app to test the functionality for more than one user. Or, if you have a Stud.IP account of the University of Osnabruck, you can use those credentials to log into the app.
