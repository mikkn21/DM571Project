# Dependencies
python=3.11
bcrypt=4.0.1

# TODO: database
- we need to make sure that members, shifts and shows, gets an id base on the online database. 



# Run Test
```
python manage.py test
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