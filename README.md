# Flask API (Flask, Postgres, SQLAlchemy, Redis)

## Steps to run app

1. Clone the repository

2. Get a working `.env` file. There is a template to follow which is `.env.sample`

### If you want to run inside containers

3. RUN `docker-compose up` - expects you to have docker installed

### If not running inside containers

3. `cd` into the cloned repo and RUN `pip3 install -r requirements.txt` to install all the necessary dependencies

4. Make sure you have PostgresDB installed and running 

5. RUN `FLASK_APP=manager.py flask db upgrade` to execute the migrations

6. RUN `python3 manager.py run` to launch the server


## How to use the app

### API documentation is hosted at the homepage
