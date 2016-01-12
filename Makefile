install:
	pip install -r requirements/production.txt
	
test:
	python manage.py test
	
login:
	ssh ubuntu@52.71.97.249
	
assets:
	python manage.py collectstatic --noi