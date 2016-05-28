init:
	pip install -r requirements.txt

.PHONY: test

test:
	python -m unittest discover -s test -p "Test*.py"
