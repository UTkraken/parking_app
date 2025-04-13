# ParkDashboard 

> Parking Management Application using DRF and Vuejs

## Getting started
### Requirements
* Python 3.11
* Node v20.18.0

### Installations

#### Front
``cd front/parking``

``npm install``

``npm run dev``

#### Back

``cd back/parking``

```py -m venv .venv```

```.venv\Scripts\activate```

```py -m pip install -r requirements.txt```

create a local database with postgresql named 'parking'
* user = postgres
* password = postgres 
* host = localhost
* port = 5432

``py manage.py add_data``

``py manage.py runserver``