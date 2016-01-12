install:
	pip install -r requirements/production.txt
	
test:
	python manage.py test
	
static:
	python manage.py collectstatic --noi