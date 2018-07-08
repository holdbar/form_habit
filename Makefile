
create-virtualenv:
	virtualenv -p python3 .env

pip-install:
	pip install -r requirements.txt

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations

createsuperuser:
	python manage.py createsuperuser

runserver:
	python manage.py runserver 0.0.0.0:8080
