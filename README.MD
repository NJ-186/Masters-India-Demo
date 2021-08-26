# Masters India Demo

## Overview :-
This is a demo project.


## INSTALLATION :-
1. Clone the repo in your local system.

2. Create a virtual environment.
    - MAC users :-
        Refer to :- https://gist.github.com/pandafulmanda/730a9355e088a9970b18275cb9eadef3

    - Windows and Linux users :-
        Refer to :- https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/

3. Install Requirements
    Change directory to the root folder and run
    
    `pip install -r requirements.txt` 

4. Make migrations and migrate.
    Run these commands

    `python manage.py makemigrations` and `python manage.py migrate`

5. Start the server.

    `python manage.py runserver`

6. You are good to go. Happy hacking !


## API Description :- 
1. Homepage :- http://127.0.0.1:8000

2. Get All Categories :- http://127.0.0.1:8000/getAllCategories

3. Get All Sub-Categories for a particular Category :- http://127.0.0.1:8000/getAllSubCategories

4. Get All Products for a particular Category :- http://127.0.0.1:8000/getAllProductsForCategory

5. Get All Products for a particular Sub-Category :- http://127.0.0.1:8000/getAllProductsForSubCategory

6. Post Product for a given Category and Sub-Category :- http://127.0.0.1:8000/postProduct

Note :- The details on each request could be found in the postman collection file ( -> Masters India.postman_collection.json )