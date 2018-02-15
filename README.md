# Grain
Welcome to Gramedia Inventory Manager API. This app implement to managing inventory for office.

## Preparing
In this app need some packages as a Django dependencies. Type the following command:

```
$ pip install -r requirements.txt
$ python manage.py migrate
```

## Test
You can very easy to test this app with the following command:

```
$ python manage.py test
```

## Load Initial Data
For sample data, you can loaded initial data with the following command:

```
$ python manage.py loaddata company.yaml
$ python manage.py loaddata division.yaml
$ python manage.py loaddata user.yaml
$ python manage.py loaddata employee.yaml
```

