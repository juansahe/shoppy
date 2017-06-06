
#ShopperMiles


# Prerequisites 
- [virtualenv](https://virtualenv.pypa.io/en/latest/)

# Initialize the project
Create and activate a virtualenv:

```bash
virtualenv env --no-site-packages --distribute -p /usr/local/bin/python3
or
pyvenv env
source env/bin/activate
```
Install dependencies:

```bash
pip install -r requirements.txt
```

Initialize the git repository

```bash
git init
git remote add origin git@github.com:andresvz/ShopperMiles.git
```

Migrate, create a superuser, and run the server:

```bash
python ShopperMiles/manage.py migrate
python ShopperMiles/manage.py createsuperuser
python ShopperMiles/manage.py runserver
```

Generate API docs:

```bash
npm install apidoc -g
python ShopperMiles/manage.py apidoc 
```
