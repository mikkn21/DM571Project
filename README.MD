# Install Dependencies
Use python version 3.11, and then execute the below command:
```
pip install -r requirements.txt
```

# Logins 

To help with testing, we have implemented a `dummy_database.py` that includes some users:
- Sales user:
    - E-Mail: sales@gmail.com
    - Password: sales
- PR user:
    - E-Mail: pr@gmail.com
    - Password: pr
- Super user:
    - E-Mail: admin@gmail.com
    - Password: admin
    - Note that this user is a Super user and is not a part o any group themselves.

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

# To Generate coverage report run:
```
coverage run --source='.' manage.py test website
```

# To view the coverage report
```
coverage report
```

# For a more detailed HTML report, run:
```
coverage html
```
