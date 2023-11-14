# Install Dependencies
Use python version 3.11, and then execute the below command:
```
pip install -r requirements.txt
```

# TODO: database
- we need to make sure that members, shifts and shows, gets an id base on the online database. 



# Run Test
```
python manage.py test
```

# Run specific test
```
python manage.py test tests.test_models
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
