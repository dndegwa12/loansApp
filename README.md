# loansApp
Every two months we are given a text file from our accounting department detailing all the loans given out on our networks. This needs to be a validated against our internal systems by the tuple of (Network, Product, Month). This projects aggregates the loan data by the tuple of (Network, Product, Month) with sum amounts and counts and outputs into a csv file.

Installation
git clone https://github.com/dndegwa12/loansApp.git

Create a virtualenv in the project directory

cd loans

virtualenv venv

source venv/bin/activate
Installing dependencies
pip install -r requirements.txt

Configure celery
Edit celery configuration in app/celery.py

Start celery
On one terminal
celery -A app worker --loglevel=info

Start application
On another terminal
python run.py

Assumptions
RabbitMQ had been configured on the server
CSV has no missing values
CSV is automatically pushed to the data folder
Aggregated outputs are needed on demand
This is just a microservice which is part of a larger system
Stack
Built on python - multi-paradigm language which supports functional, procedural and object oriented programming styles.

Key Libraries of this stack include -:

Celery is an asynchronous task queue. Ideal for background computation of expensive queries. This will make it easier to scale our computation capacity e.g. aggregate summaries for the last 10 years will probably be from a csv with several millions rows.
RabbitMQ is a message broker used with Celery.
Logging – Allows logging program’s execution to a file
CSV - library that implements classes to read and write tabular data in CSV format
