# Install Dependencies
Use python version 3.11, and then execute the below command:
```
pip install -r requirements.txt
```

# TODO: database
- we need to make sure that members, shifts and shows, gets an id base on the online database. 

# How to make test
Make a file in the website/tests folder and it will be run by the tests.
You are allowed to make subdirectories and make test in them too, as long as you also add an __init__.py file in that directory. 

# Run Test
```
python manage.py test website
```

# Run specific test
```
python manage.py test website.tests.test_models
```


# Checking Test Coverage
```
coverage run --source='.' manage.py test
```

# To view the coverage report
```
coverage report
```

# For a more detailed HTML report, run:
```
coverage html
```
