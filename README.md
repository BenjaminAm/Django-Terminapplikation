# bachelor-arbeit

To set up and start the project follow these steps:

- clone the repository.
- run one of these commands to activate the python virtual environment depending on your OS and shell:

## POSIX:
- bash/zsh:          $ source termin_app_project/venv/bin/activate
- fish:              $ source termin_app_project/venv/bin/activate.fish
- csh/tcsh:          $ source termin_app_project/venv/bin/activate.csh
- PowerShell Core:   $ termin_app_project/venv/bin/Activate.ps1

## Windows:
- cmd.exe:           C:\> termin_app_project\venv\Scripts\activate.bat
- PowerShell:        PS C:\> termin_app_project\venv\Scripts\Activate.ps1
        
        
- run "python manage.py makemigrations" and "python manage.py migrate" to create the database.
- run "python manage.py createsuperuser" to create an admin user.
- run "python manage.py runserver" to run the app with the django dev server.
- you can log in with the admin account and take a look at the app. Alternatively you can log into the django admin backend at /admin with the admin account 
and create other users. With these you can then log into the main app to test the functionality for more than one user.
