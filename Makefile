install:
	pip install -r requiremnents/production.txt
	
test:
	python manage.py test
	
static:
	python manage.py collectstatic --noi