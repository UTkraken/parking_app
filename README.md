# ParkDashboard 

> Parking Management Application using DRF and Vuejs

## Getting started
### Requirements
* Python 3.11
* Node v20.18.0

### Installations

#### Back

``cd back/parking``

##### Create a virtual environment

```py -m venv .venv```

```.venv\Scripts\activate```

##### Upgrade pip 

``py -m pip install --upgrade pip``

##### Install dependancies

```py -m pip install -r requirements.txt```

##### Create database

create a local database with postgresql named 'parking'
* user = postgres
* password = postgres 
* host = localhost
* port = 5432

Or change informations in settings.py

##### Apply migrations

``py manage.py migrate``

##### Populate database

``py manage.py add_data``

##### Create superuser for login

``py manage.py createsuperuser``

##### Run server !!

``py manage.py runserver``

#### Front
``cd front/parking``

``npm install``

``npm run dev``

