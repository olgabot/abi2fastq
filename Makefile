help:
	@echo "lint - check code style with flake8"
	@echo "test - run tests only"
	@echo "coverage - run tests and check code coverage"

test:
	py.test

coverage:
	coverage run --source abi2fastq --omit="*/test*" --module py.test
	coverage report --show-missing

lint:
	flake8 --exclude docs abi2fastq

pypi:
	python setup.py sdist upload