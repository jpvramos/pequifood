clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*.~' -exec rm -f {} \;
	rm -fr .cache
	rm -fr build
	rm -fr dist
	rm -fr *.egg-info
	rm -fr htmlcov
	rm -fr .tox/
	rm -fr docs/.build
	pip install -e .['dev'] --upgrade --no-cache

install:
	pip install -e .['dev']

init_db:
	FLASK_APP=pequifood/app.py flask create-db
	FLASK_APP=pequifood/app.py flask db

test:
	FLASK_ENV=test pytest tests/ -v --cov=pequifood

format:
	isort **/*.py
	black -l 79 **/*.py


run:
	Set FLASK_APP="pequifood\\app.py"
	Set FLASK_ENV="development"
	flask run
