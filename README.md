# Message App

## Setup

- Checkout the repository
    > Pull the latest changes if you already have it

- Create virtual environment using shell

    `virtualenv venv`

    or using PyCharm:
    
    `Settings > Project > Project Interpreter > Add... > Virtual Environment > New Environment`

- Install requirements

    `pip install -r requirements.txt`

- Apply migrations

    `python manage.py migrate`

- Start the app to make sure everything went well

    `python manage.py runserver`

    or using PyCharm run configuration

## Todo

- Create campaigns app

    `django-admin startapp campaigns`

    This creates a new directory called `campaings` where you will do most of the work

- Look inside the project for `Todo (Mentee)`
