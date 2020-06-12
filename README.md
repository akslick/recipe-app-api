# recipe-app-api
Recipie app api source code


https://www.udemy.com/course/django-python-advanced

https://github.com/LondonAppDeveloper/recipe-app-api

To run a command in a docker container from the compose

    docker-compose run app sh -c "django-admin.py startproject app .
    
    docker-compose run app sh -c "python manage.py startapp core"


To Run tests and linter

    docker-compose run app sh -c "python manage.py test  && flake8


Has custome User model