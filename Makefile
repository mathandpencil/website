install:
	pip install -r requirements/production.txt
	
test:
	python manage.py test
	
assets:
	python manage.py collectstatic --noi