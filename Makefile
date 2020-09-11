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
